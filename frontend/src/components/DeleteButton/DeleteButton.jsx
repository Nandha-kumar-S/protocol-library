import React, { useState } from 'react'
import styled from 'styled-components'
import { FiTrash2, FiAlertTriangle } from 'react-icons/fi'

const DeleteButtonContainer = styled.div`
  position: relative;
  display: inline-block;
`

const DeleteBtn = styled.button`
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &:hover {
    background: #c82333;
    transform: translateY(-1px);
  }
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
  }
  
  &.small {
    padding: 4px 8px;
    font-size: 0.75rem;
  }
  
  &.icon-only {
    padding: 8px;
    
    &.small {
      padding: 4px;
    }
  }
`

const ConfirmationModal = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
`

const ModalContent = styled.div`
  background: white;
  border-radius: 8px;
  padding: 24px;
  max-width: 400px;
  width: 90%;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
`

const ModalHeader = styled.div`
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  
  svg {
    color: #dc3545;
    width: 24px;
    height: 24px;
  }
`

const ModalTitle = styled.h3`
  margin: 0;
  color: #495057;
  font-size: 1.1rem;
`

const ModalMessage = styled.p`
  margin: 0 0 20px 0;
  color: #6c757d;
  line-height: 1.5;
`

const ModalActions = styled.div`
  display: flex;
  gap: 12px;
  justify-content: flex-end;
`

const ModalButton = styled.button`
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &.cancel {
    background: #6c757d;
    color: white;
    
    &:hover {
      background: #545b62;
    }
  }
  
  &.confirm {
    background: #dc3545;
    color: white;
    
    &:hover {
      background: #c82333;
    }
  }
`

const DeleteButton = ({
  onDelete,
  confirmMessage = 'Are you sure you want to delete this item?',
  confirmTitle = 'Confirm Delete',
  disabled = false,
  size = 'normal', // 'normal' | 'small'
  variant = 'default', // 'default' | 'icon-only'
  children = 'Delete',
  className = ''
}) => {
  const [showConfirmation, setShowConfirmation] = useState(false)
  const [isDeleting, setIsDeleting] = useState(false)

  const handleDeleteClick = () => {
    setShowConfirmation(true)
  }

  const handleConfirm = async () => {
    setIsDeleting(true)
    try {
      await onDelete()
      setShowConfirmation(false)
    } catch (error) {
      console.error('Delete failed:', error)
    } finally {
      setIsDeleting(false)
    }
  }

  const handleCancel = () => {
    setShowConfirmation(false)
  }

  const buttonClasses = [
    size === 'small' ? 'small' : '',
    variant === 'icon-only' ? 'icon-only' : '',
    className
  ].filter(Boolean).join(' ')

  return (
    <DeleteButtonContainer>
      <DeleteBtn
        onClick={handleDeleteClick}
        disabled={disabled || isDeleting}
        className={buttonClasses}
      >
        <FiTrash2 size={size === 'small' ? 12 : 14} />
        {variant !== 'icon-only' && (
          <span>{isDeleting ? 'Deleting...' : children}</span>
        )}
      </DeleteBtn>

      {showConfirmation && (
        <ConfirmationModal onClick={handleCancel}>
          <ModalContent onClick={(e) => e.stopPropagation()}>
            <ModalHeader>
              <FiAlertTriangle />
              <ModalTitle>{confirmTitle}</ModalTitle>
            </ModalHeader>
            <ModalMessage>{confirmMessage}</ModalMessage>
            <ModalActions>
              <ModalButton 
                className="cancel" 
                onClick={handleCancel}
                disabled={isDeleting}
              >
                Cancel
              </ModalButton>
              <ModalButton 
                className="confirm" 
                onClick={handleConfirm}
                disabled={isDeleting}
              >
                {isDeleting ? 'Deleting...' : 'Delete'}
              </ModalButton>
            </ModalActions>
          </ModalContent>
        </ConfirmationModal>
      )}
    </DeleteButtonContainer>
  )
}

export default DeleteButton
