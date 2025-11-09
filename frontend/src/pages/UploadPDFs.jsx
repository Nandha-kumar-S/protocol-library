import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import styled from 'styled-components'
import { FiUpload, FiFile, FiX, FiCheck, FiClock, FiCheckCircle, FiPauseCircle } from 'react-icons/fi'
import { jobAPI, protocolAPI } from '../services/api';
import { useToast } from '../contexts/ToastContext';

const PageContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
`

const PageTitle = styled.h1`
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 30px;
  font-weight: 600;
`

const JobCountsSection = styled.div`
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 30px;
  width: 100%;
`

const NotificationCard = styled.div`
  background: ${props => getBackgroundColor(props.type)};
  border-radius: 12px;
  border-left: 4px solid ${props => getBorderColor(props.type)};
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 20px 24px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 16px;
  
  &:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  }
`

const JobStatusRow = styled.div`
  display: flex;
  gap: 16px;
  width: 100%;
  flex-wrap: wrap;
`

const StatusCard = styled(NotificationCard)`
  flex: 1;
  min-width: 250px;
  margin: 0;
`

const getBorderColor = (type) => {
  switch (type) {
    case 'paused': return '#F59E0B';
    case 'completed': return '#10B981';
    default: return '#3B82F6';
  }
};

const getBackgroundColor = (type) => {
  return type === 'paused' ? '#FFFBEB' : 'white';
};

const getIconBackground = (type) => {
  switch (type) {
    case 'paused': return '#F59E0B';
    case 'completed': return '#10B981';
    default: return '#3B82F6';
  }
};

const getBadgeStyles = (type) => {
  const styles = {
    background: '',
    color: ''
  };

  if (type === 'paused') {
    styles.background = '#FEF3C7';
    styles.color = '#92400E';
  } else if (type === 'completed') {
    styles.background = '#D1FAE5';
    styles.color = '#065F46';
  } else {
    styles.background = '#DBEAFE';
    styles.color = '#1E40AF';
  }

  return styles;
};


const NotificationIcon = styled.div`
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: white;
  background: ${props => getIconBackground(props.type)};
  flex-shrink: 0;
`

const NotificationContent = styled.div`
  flex: 1;
`

const NotificationTitle = styled.div`
  font-weight: 600;
  color: #1F2937;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 8px;
`

const NotificationBadge = styled.span`
  background: ${props => getBadgeStyles(props.type).background};
  color: ${props => getBadgeStyles(props.type).color};
  font-size: 0.75rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 9999px;
`

const NotificationMessage = styled.div`
  font-size: 0.875rem;
  color: #4B5563;
`

const JobCountHeader = styled.div`
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
`

const JobCountIcon = styled.div`
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: white;
  margin-right: 16px;

  &.in-progress {
    background-color: #3b82f6;
  }

  &.completed {
    background-color: #10b981;
  }
  
  &.paused {
    background-color: #f59e0b;
  }
`

const JobCountInfo = styled.div`
  flex: 1;
`

const JobCountNumber = styled.div`
  font-size: 1.8rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 4px;
`

const JobCountLabel = styled.div`
  font-size: 0.9rem;
  color: #6c757d;
  text-transform: uppercase;
  letter-spacing: 0.5px;
`

const UploadSection = styled.div`
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 40px;
  margin-bottom: 30px;
`

const DropZone = styled.div`
  border: 2px dashed #dee2e6;
  border-radius: 12px;
  padding: 60px 20px;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  
  &:hover {
    border-color: #007bff;
    background: #f8f9ff;
  }
  
  &.dragover {
    border-color: #007bff;
    background: #f0f8ff;
  }
`

const UploadIcon = styled.div`
  font-size: 3rem;
  color: #6c757d;
  margin: 0 auto 20px auto;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
`;

const UploadText = styled.div`
  font-size: 1.2rem;
  color: #495057;
  margin-bottom: 10px;
`

const UploadSubtext = styled.div`
  font-size: 0.9rem;
  color: #6c757d;
`

const FileInput = styled.input`
  display: none;
`

const UploadButton = styled.button`
  background: #007bff;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 20px;
  transition: background 0.3s ease;
  
  &:hover {
    background: #0056b3;
  }
`

const FileList = styled.div`
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
`

const FileListHeader = styled.div`
  background: #f8f9fa;
  padding: 20px;
  border-bottom: 1px solid #dee2e6;
`

const FileListTitle = styled.h2`
  margin: 0;
  font-size: 1.3rem;
  color: #2c3e50;
`

const FileItem = styled.div`
  display: flex;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid #f1f3f4;
  
  &:last-child {
    border-bottom: none;
  }
`

const FileIcon = styled.div`
  width: 40px;
  height: 40px;
  background: #e3f2fd;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 16px;
  color: #1976d2;
`

const FileInfo = styled.div`
  flex: 1;
`

const FileName = styled.div`
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 4px;
`

const FileSize = styled.div`
  font-size: 0.8rem;
  color: #6c757d;
`

const FileActions = styled.div`
  display: flex;
  gap: 8px;
`

const ActionButton = styled.button`
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &.remove {
    background: #fee;
    color: #dc3545;
    
    &:hover {
      background: #fdd;
    }
  }
  
  &.success {
    background: #efe;
    color: #28a745;
  }
`

const UploadPDFs = () => {
  const navigate = useNavigate()
  const [files, setFiles] = useState([])
  const [dragOver, setDragOver] = useState(false)
  const [jobCounts, setJobCounts] = useState({
    inProgress: 0,
    completed: 0,
    paused: 0
  });
  
  const { showSuccess, showError } = useToast();

  useEffect(() => {
    const fetchJobCounts = async () => {
      try {
        const response = await protocolAPI.getDashboardStatus()
        const statusCounts = response.data

        // Calculate in-progress count
        const inProgressCount = [
          "STARTED",
          "PARSING",
          "PREPROCESSING",
          "MAP_SECTIONS_TO_SCHEMAS",
          "CONTENT_EXTRACTION",
          "CONTENT_EXTRACTION_PAUSED",
          "MAP_CONTENT_TO_SCHEMAS",
          "CONNECT_SCHEMAS",
          "LINK_SCHEMAS",
          "FAILED"
        ].reduce((sum, status) => sum + (statusCounts[status] || 0), 0)

        // Get completed and paused counts
        const completedCount = statusCounts['COMPLETED'] || 0
        const pausedCount = statusCounts['CONTENT_EXTRACTION_PAUSED'] || 0

        setJobCounts({
          inProgress: inProgressCount,
          completed: completedCount,
          paused: pausedCount
        })
      } catch (error) {
        console.error('Error fetching job counts:', error)
      }
    }

    fetchJobCounts()
  }, [])

  const handleFileSelect = (selectedFiles) => {
    const newFiles = Array.from(selectedFiles).map(file => ({
      id: Date.now() + Math.random(),
      file,
      name: file.name,
      size: formatFileSize(file.size),
      uploaded: false
    }))
    setFiles(prev => [...prev, ...newFiles])
  }

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes'
    const k = 1024
    const sizes = ['Bytes', 'KB', 'MB', 'GB']
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setDragOver(false)
    const droppedFiles = e.dataTransfer.files
    handleFileSelect(droppedFiles)
  }

  const handleDragOver = (e) => {
    e.preventDefault()
    setDragOver(true)
  }

  const handleDragLeave = (e) => {
    e.preventDefault()
    setDragOver(false)
  }

  const removeFile = (fileId) => {
    setFiles(prev => prev.filter(f => f.id !== fileId))
  }

  const uploadFile = async (fileId) => {
    try {
      const fileToUpload = files.find(f => f.id === fileId);
      if (!fileToUpload) return;

      const formData = new FormData();
      formData.append('file', fileToUpload.file);

      await jobAPI.uploadPDFs(formData);
      setFiles(prev => prev.map(f =>
        f.id === fileId ? { ...f, uploaded: true } : f
      ));

      // Show success message
      showSuccess('The uploaded document will be processed as a background job. Please check the job status in the All Jobs menu.');

      // Refresh job counts
      await fetchJobCounts();
    } catch (error) {
      console.error('Error uploading file:', error);
      showError('Error uploading file');
    }
  };


  const fetchJobCounts = async () => {
    try {
      const response = await protocolAPI.getDashboardStatus()
      const statusCounts = response.data;
      // Calculate in-progress count
      const inProgressCount = [
        "STARTED",
        "PARSING",
        "PREPROCESSING",
        "MAP_SECTIONS_TO_SCHEMAS",
        "CONTENT_EXTRACTION",
        "CONTENT_EXTRACTION_PAUSED",
        "MAP_CONTENT_TO_SCHEMAS",
        "CONNECT_SCHEMAS",
        "LINK_SCHEMAS",
        "FAILED"
      ].reduce((sum, status) => sum + (statusCounts[status] || 0), 0)

      // Get completed and paused counts
      const completedCount = statusCounts['COMPLETED'] || 0
      const pausedCount = statusCounts['CONTENT_EXTRACTION_PAUSED'] || 0

      setJobCounts({
        inProgress: inProgressCount,
        completed: completedCount,
        paused: pausedCount
      })
    } catch (error) {
      console.error('Error fetching job counts:', error)
    }
  }

  return (
    <PageContainer>
      <JobCountsSection>
        <JobStatusRow>
          {jobCounts.paused > 0 && (
            <StatusCard
              type="paused"
              onClick={() => navigate('/jobs?status=PAUSED')}
            >
              <NotificationIcon type="paused">
                <FiPauseCircle />
              </NotificationIcon>
              <NotificationContent>
                <NotificationTitle>
                  Action Required
                  <NotificationBadge type="paused">
                    {jobCounts.paused} {jobCounts.paused === 1 ? 'job' : 'jobs'} waiting
                  </NotificationBadge>
                </NotificationTitle>
                <NotificationMessage>
                  Review and action required for {jobCounts.paused} {jobCounts.paused === 1 ? 'job' : 'jobs'}
                </NotificationMessage>
              </NotificationContent>
            </StatusCard>
          )}

          <StatusCard
            type="inProgress"
            onClick={() => navigate('/jobs?status=IN_PROGRESS')}
          >
            <NotificationIcon type="inProgress">
              <FiClock />
            </NotificationIcon>
            <NotificationContent>
              <NotificationTitle>In Progress</NotificationTitle>
              <NotificationMessage>
                {jobCounts.inProgress} {jobCounts.inProgress === 1 ? 'job' : 'jobs'} processing
              </NotificationMessage>
            </NotificationContent>
          </StatusCard>

          <StatusCard
            type="completed"
            onClick={() => navigate('/jobs?status=COMPLETED')}
          >
            <NotificationIcon type="completed">
              <FiCheckCircle />
            </NotificationIcon>
            <NotificationContent>
              <NotificationTitle>Completed</NotificationTitle>
              <NotificationMessage>
                {jobCounts.completed} {jobCounts.completed === 1 ? 'job' : 'jobs'} done
              </NotificationMessage>
            </NotificationContent>
          </StatusCard>
        </JobStatusRow>
      </JobCountsSection>

      <UploadSection>
        <DropZone
          className={dragOver ? 'dragover' : ''}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onClick={() => document.getElementById('fileInput').click()}
        >
          <UploadIcon>
            <FiUpload />
          </UploadIcon>
          <UploadText>Drag and drop PDF files here</UploadText>
          <UploadSubtext>or click to browse files</UploadSubtext>
          <UploadButton type="button">
            Choose Files
          </UploadButton>
        </DropZone>

        <FileInput
          id="fileInput"
          type="file"
          multiple
          accept=".pdf"
          onChange={(e) => handleFileSelect(e.target.files)}
        />
      </UploadSection>

      {files.length > 0 && (
        <FileList>
          <FileListHeader>
            <FileListTitle>Uploaded Files ({files.length})</FileListTitle>
          </FileListHeader>
          {files.map(file => (
            <FileItem key={file.id}>
              <FileIcon>
                <FiFile />
              </FileIcon>
              <FileInfo>
                <FileName>{file.name}</FileName>
                <FileSize>{file.size}</FileSize>
              </FileInfo>
              <FileActions>
                {file.uploaded ? (
                  <ActionButton className="success">
                    <FiCheck />
                  </ActionButton>
                ) : (
                  <ActionButton onClick={() => uploadFile(file.id)}>
                    <FiUpload />
                  </ActionButton>
                )}
                <ActionButton className="remove" onClick={() => removeFile(file.id)}>
                  <FiX />
                </ActionButton>
              </FileActions>
            </FileItem>
          ))}
        </FileList>
      )}
    </PageContainer>
  )
}

export default UploadPDFs
