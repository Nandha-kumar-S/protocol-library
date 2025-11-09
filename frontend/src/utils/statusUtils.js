// Status mapping from backend codes to display names
export const STATUS_MAPPING = {
  "STARTED": "Started",
  "PARSING": "Document Analysis",
  "PREPROCESSING": "Document Analysis", 
  "MAP_SECTIONS_TO_SCHEMAS": "Document Analysis",
  "CONTENT_EXTRACTION": "Extracting Protocol Details",
  "CONTENT_EXTRACTION_PAUSED": "Extracting Protocol Details",
  "MAP_CONTENT_TO_SCHEMAS": "Standardising to schemas",
  "MAP_CONTENT_TO_SCHEMAS_PAUSED": "Standardising to schemas",
  "CONNECT_SCHEMAS": "Generating Network",
  "LINK_SCHEMAS": "Generating Network",
  "COMPLETED": "Completed",
  "FAILED": "Failed"
}

// Status stages for roadmap display
export const STATUS_STAGES = [
  { 
    key: "Started", 
    label: "Started", 
    color: "#28a745",
    description: "Job has been initiated"
  },
  { 
    key: "Document Analysis", 
    label: "Document Analysis", 
    color: "#17a2b8",
    description: "Parsing and preprocessing document"
  },
  { 
    key: "Extracting Protocol Details", 
    label: "Extracting Protocol Details", 
    color: "#ffc107",
    description: "Extracting content from document"
  },
  { 
  key: "Standardising to schemas", 
  label: "Standardising to schemas", 
    color: "#fd7e14",
  description: "Mapping content to schemas"
  },
  { 
  key: "Generating Network", 
  label: "Generating Network", 
    color: "#6f42c1",
    description: "Connecting and linking schemas"
  },
  { 
    key: "Completed", 
    label: "Completed", 
    color: "#28a745",
    description: "Job completed successfully"
  },
  { 
    key: "Failed", 
    label: "Failed", 
    color: "#dc3545",
    description: "Job failed during processing"
  }
]

// Get display status from backend status
export const getDisplayStatus = (backendStatus) => {
  return STATUS_MAPPING[backendStatus] || backendStatus
}

// Get current stage index for progress calculation
export const getCurrentStageIndex = (status) => {
  const displayStatus = getDisplayStatus(status)
  return STATUS_STAGES.findIndex(stage => stage.key === displayStatus)
}

// Calculate progress percentage
export const getProgressPercentage = (status) => {
  const currentIndex = getCurrentStageIndex(status)
  if (currentIndex === -1) return 0
  if (status === 'FAILED') return 100 // Show full progress for failed jobs
  return ((currentIndex + 1) / STATUS_STAGES.length) * 100
}

// Get status color based on current status
export const getStatusColor = (status) => {
  const displayStatus = getDisplayStatus(status)
  const stage = STATUS_STAGES.find(stage => stage.key === displayStatus)
  return stage ? stage.color : '#6c757d'
}

// Check if status is in progress
export const isStatusInProgress = (status) => {
  return !['COMPLETED', 'FAILED'].includes(status)
}

// Get status category
export const getStatusCategory = (status) => {
  if (status === 'COMPLETED') return 'completed'
  if (status === 'FAILED') return 'failed'
  return 'in-progress'
}

// Format date for display
export const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// Calculate time elapsed
export const getTimeElapsed = (startDate) => {
  if (!startDate) return 'N/A'
  
  const start = new Date(startDate)
  const now = new Date()
  const diff = Math.floor((now - start) / (1000 * 60)) // difference in minutes
  
  if (diff < 1) {
    return 'Just now'
  } else if (diff < 60) {
    return `${diff}m`
  } else {
    const hours = Math.floor(diff / 60)
    const minutes = diff % 60
    return `${hours}h ${minutes}m`
  }
}
