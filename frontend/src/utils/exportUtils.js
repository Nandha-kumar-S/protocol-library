// Utility functions for data export functionality

/**
 * Convert data to CSV format
 */
export const convertToCSV = (data, headers = null) => {
  if (!data || data.length === 0) return ''
  
  // Auto-generate headers if not provided
  if (!headers) {
    headers = Object.keys(data[0])
  }
  
  // Create CSV header row
  const csvHeaders = headers.join(',')
  
  // Create CSV data rows
  const csvRows = data.map(item => {
    return headers.map(header => {
      const value = item[header]
      // Handle nested objects and arrays
      if (typeof value === 'object' && value !== null) {
        return `"${JSON.stringify(value).replace(/"/g, '""')}"`
      }
      // Escape commas and quotes in strings
      if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
        return `"${value.replace(/"/g, '""')}"`
      }
      return value || ''
    }).join(',')
  })
  
  return [csvHeaders, ...csvRows].join('\n')
}

/**
 * Convert data to JSON format with pretty printing
 */
export const convertToJSON = (data) => {
  return JSON.stringify(data, null, 2)
}

/**
 * Download data as a file
 */
export const downloadFile = (content, filename, contentType = 'text/plain') => {
  const blob = new Blob([content], { type: contentType })
  const url = window.URL.createObjectURL(blob)
  
  const link = document.createElement('a')
  link.href = url
  link.download = filename
  document.body.appendChild(link)
  link.click()
  
  // Cleanup
  document.body.removeChild(link)
  window.URL.revokeObjectURL(url)
}

/**
 * Export protocols to CSV
 */
export const exportProtocolsToCSV = (protocols) => {
  const headers = ['id', 'title', 'description', 'createdAt', 'updatedAt']
  const csvData = protocols.map(protocol => ({
    id: protocol.id,
    title: protocol.title,
    description: protocol.description,
    createdAt: protocol.createdAt,
    updatedAt: protocol.updatedAt
  }))
  
  const csv = convertToCSV(csvData, headers)
  const filename = `protocols_${new Date().toISOString().split('T')[0]}.csv`
  downloadFile(csv, filename, 'text/csv')
}

/**
 * Export studies to CSV
 */
export const exportStudiesToCSV = (studies) => {
  const headers = ['id', 'title', 'description', 'participants', 'startDate', 'endDate', 'status']
  const csvData = studies.map(study => ({
    id: study.id,
    title: study.title,
    description: study.description,
    participants: study.participants,
    startDate: study.startDate,
    endDate: study.endDate,
    status: study.status
  }))
  
  const csv = convertToCSV(csvData, headers)
  const filename = `studies_${new Date().toISOString().split('T')[0]}.csv`
  downloadFile(csv, filename, 'text/csv')
}

/**
 * Export jobs to CSV
 */
export const exportJobsToCSV = (jobs) => {
  const headers = ['id', 'title', 'description', 'status', 'progress', 'createdAt']
  const csvData = jobs.map(job => ({
    id: job.id,
    title: job.title,
    description: job.description,
    status: job.status,
    progress: job.progress,
    createdAt: job.createdAt
  }))
  
  const csv = convertToCSV(csvData, headers)
  const filename = `jobs_${new Date().toISOString().split('T')[0]}.csv`
  downloadFile(csv, filename, 'text/csv')
}

/**
 * Export data to JSON
 */
export const exportToJSON = (data, filename) => {
  const json = convertToJSON(data)
  const fullFilename = filename.endsWith('.json') ? filename : `${filename}.json`
  downloadFile(json, fullFilename, 'application/json')
}

/**
 * Export complete protocol library data
 */
export const exportCompleteData = (protocols, studies, jobs) => {
  const completeData = {
    exportDate: new Date().toISOString(),
    version: '1.0.0',
    data: {
      protocols,
      studies,
      jobs
    },
    summary: {
      protocolCount: protocols.length,
      studyCount: studies.length,
      jobCount: jobs.length
    }
  }
  
  const filename = `protocol_library_export_${new Date().toISOString().split('T')[0]}.json`
  exportToJSON(completeData, filename)
}
