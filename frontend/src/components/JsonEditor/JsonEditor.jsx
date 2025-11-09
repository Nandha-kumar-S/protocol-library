import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import styled from 'styled-components'
import { Editor } from '@monaco-editor/react'
import { FiSave, FiRefreshCw, FiCheck, FiX } from 'react-icons/fi'
import { updateJsonEditorData } from '../../store/slices/protocolSlice'

const EditorContainer = styled.div`
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  height: ${props => props.height || '400px'};
  display: flex;
  flex-direction: column;
`

const EditorHeader = styled.div`
  display: flex;
  justify-content: between;
  align-items: center;
  padding: 12px 16px;
  background: #f8f9fa;
  border-bottom: 1px solid #e9ecef;
`

const EditorTitle = styled.h3`
  margin: 0;
  font-size: 1rem;
  color: #495057;
  flex: 1;
`

const EditorActions = styled.div`
  display: flex;
  gap: 8px;
`

const ActionButton = styled.button`
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &.primary {
    background: #007bff;
    color: white;
    
    &:hover {
      background: #0056b3;
    }
  }
  
  &.secondary {
    background: #6c757d;
    color: white;
    
    &:hover {
      background: #545b62;
    }
  }
  
  &.success {
    background: #28a745;
    color: white;
  }
  
  &.danger {
    background: #dc3545;
    color: white;
  }
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`

const EditorContent = styled.div`
  flex: 1;
  position: relative;
`

const StatusBar = styled.div`
  padding: 8px 16px;
  background: #f8f9fa;
  border-top: 1px solid #e9ecef;
  font-size: 0.875rem;
  color: #6c757d;
  display: flex;
  justify-content: space-between;
  align-items: center;
`

const ValidationStatus = styled.span`
  display: flex;
  align-items: center;
  gap: 4px;
  
  &.valid {
    color: #28a745;
  }
  
  &.invalid {
    color: #dc3545;
  }
`

const JsonEditor = ({ 
  initialValue = '{}', 
  onChange, 
  onSave, 
  title = 'JSON Editor',
  height = '400px',
  readOnly = false 
}) => {
  const [value, setValue] = useState(initialValue)
  const [isValid, setIsValid] = useState(true)
  const [hasChanges, setHasChanges] = useState(false)
  const [validationError, setValidationError] = useState('')
  const dispatch = useDispatch()

  useEffect(() => {
    setValue(initialValue)
  }, [initialValue])

  const validateJson = (jsonString) => {
    try {
      JSON.parse(jsonString)
      setIsValid(true)
      setValidationError('')
      return true
    } catch (error) {
      setIsValid(false)
      setValidationError(error.message)
      return false
    }
  }

  const handleEditorChange = (newValue) => {
    setValue(newValue)
    setHasChanges(newValue !== initialValue)
    
    if (newValue) {
      validateJson(newValue)
    }
    
    if (onChange) {
      onChange(newValue)
    }
    
    // Update Redux store
    dispatch(updateJsonEditorData(newValue))
  }

  const handleSave = () => {
    if (isValid && onSave) {
      onSave(value)
      setHasChanges(false)
    }
  }

  const handleReset = () => {
    setValue(initialValue)
    setHasChanges(false)
    validateJson(initialValue)
  }

  const formatJson = () => {
    try {
      const parsed = JSON.parse(value)
      const formatted = JSON.stringify(parsed, null, 2)
      setValue(formatted)
      handleEditorChange(formatted)
    } catch (error) {
      // If JSON is invalid, don't format
    }
  }

  return (
    <EditorContainer height={height}>
      <EditorHeader>
        <EditorTitle>{title}</EditorTitle>
        <EditorActions>
          <ActionButton 
            className="secondary" 
            onClick={formatJson}
            disabled={!isValid}
            title="Format JSON"
          >
            <FiRefreshCw size={14} />
            Format
          </ActionButton>
          <ActionButton 
            className="secondary" 
            onClick={handleReset}
            disabled={!hasChanges}
            title="Reset to original"
          >
            <FiX size={14} />
            Reset
          </ActionButton>
          <ActionButton 
            className="primary" 
            onClick={handleSave}
            disabled={!isValid || !hasChanges || readOnly}
            title="Save changes"
          >
            <FiSave size={14} />
            Save
          </ActionButton>
        </EditorActions>
      </EditorHeader>
      
      <EditorContent>
        <Editor
          height="100%"
          defaultLanguage="json"
          value={value}
          onChange={handleEditorChange}
          options={{
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            fontSize: 14,
            lineNumbers: 'on',
            roundedSelection: false,
            scrollbar: {
              vertical: 'visible',
              horizontal: 'visible',
            },
            theme: 'vs-light',
            automaticLayout: true,
            readOnly: readOnly,
          }}
        />
      </EditorContent>
      
      <StatusBar>
        <ValidationStatus className={isValid ? 'valid' : 'invalid'}>
          {isValid ? (
            <>
              <FiCheck size={14} />
              Valid JSON
            </>
          ) : (
            <>
              <FiX size={14} />
              {validationError}
            </>
          )}
        </ValidationStatus>
        
        <div>
          {hasChanges && <span>• Unsaved changes</span>}
        </div>
      </StatusBar>
    </EditorContainer>
  )
}

export default JsonEditor
