import axios from 'axios'
import { mockProtocols, mockJobs, mockApiResponse, mockApiError } from '../data/mockData'

// Create axios instance with base configuration
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error)
  }
)

// Mock API flag - set to true to use mock data
const USE_MOCK_API = import.meta.env.VITE_USE_MOCK_API === 'true' || false

// Protocol API
export const protocolAPI = {
  getDashboardStatus: () => {
    if (USE_MOCK_API) {
      // Create mock response in the same format as the API
      const mockStatusCounts = {
        'STARTED': 2,
        'PARSING': 1,
        'PREPROCESSING': 1,
        'MAP_SECTIONS_TO_SCHEMAS': 0,
        'CONTENT_EXTRACTION_PAUSED': 1,
        'MAP_CONTENT_TO_SCHEMAS': 0,
        'CONNECT_SCHEMAS': 0,
        'LINK_SCHEMAS': 0,
        'FAILED': 0,
        'COMPLETED': 5
      }
      return mockApiResponse(mockStatusCounts)
    }
    return api.get('/v1/jobs/dashboard/status')
  },
  getAll: () => USE_MOCK_API ? mockApiResponse(mockProtocols) : api.get('/protocols'),
  getById: (id) => USE_MOCK_API ? mockApiResponse(mockProtocols.find(p => p.id === id)) : api.get(`/protocols/${id}`),
  create: (data) => {
    if (USE_MOCK_API) {
      const newProtocol = {
        ...data,
        id: String(Date.now()),
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
      }
      mockProtocols.push(newProtocol)
      return mockApiResponse(newProtocol)
    }
    return api.post('/protocols', data)
  },
  update: (id, data) => {
    if (USE_MOCK_API) {
      const index = mockProtocols.findIndex(p => p.id === id)
      if (index !== -1) {
        mockProtocols[index] = { ...mockProtocols[index], ...data, updatedAt: new Date().toISOString() }
        return mockApiResponse(mockProtocols[index])
      }
      return mockApiError('Protocol not found')
    }
    return api.put(`/protocols/${id}`, data)
  },
  delete: (id) => {
    if (USE_MOCK_API) {
      const index = mockProtocols.findIndex(p => p.id === id)
      if (index !== -1) {
        mockProtocols.splice(index, 1)
        return mockApiResponse({ success: true })
      }
      return mockApiError('Protocol not found')
    }
    return api.delete(`/protocols/${id}`)
  },
}

// Job API
export const jobAPI = {
  uploadPDFs: (formData) => api.post('/v1/documents/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  }),
  getSchema: (documentId, schemaName) => 
    api.get(`/v1/documents/${documentId}/INDIVIDUAL_SCHEMA?schema_name=${encodeURIComponent(schemaName)}`),
  getAll: () => USE_MOCK_API ? mockApiResponse(mockJobs) : api.get('/v1/jobs'),
  getInProgress: async () => {
    try {
      const response = await api.get('/v1/jobs/');
      return {
        data: response.data.filter(job => job.status !== 'COMPLETED'),
        error: null
      };
    } catch (error) {
      console.error('Error fetching in-progress jobs:', error);
      return {
        data: [],
        error: 'Failed to load in-progress jobs'
      };
    }
  },
  getStatus: (id) => {
    if (USE_MOCK_API) {
      const job = mockJobs.find(j => j.id === id)
      if (job) {
        // Simulate status changes for in-progress jobs
        if (job.status === 'in_progress') {
          job.progress = Math.min(100, job.progress + Math.random() * 10)
          if (job.progress >= 100) {
            job.status = 'completed'
            job.completedAt = new Date().toISOString()
          }
        }
        return mockApiResponse(job)
      }
      return mockApiError('Job not found')
    }
    return api.get(`/v1/jobs/${id}/status`)
  },
  create: (data) => {
    if (USE_MOCK_API) {
      const newJob = {
        ...data,
        id: String(Date.now()),
        status: 'pending',
        progress: 0,
        createdAt: new Date().toISOString()
      }
      mockJobs.push(newJob)
      return mockApiResponse(newJob)
    }
    return api.post('/v1/jobs', data)
  },
  update: (id, data) => {
    if (USE_MOCK_API) {
      const index = mockJobs.findIndex(j => j.id === id)
      if (index !== -1) {
        mockJobs[index] = { ...mockJobs[index], ...data, updatedAt: new Date().toISOString() }
        return mockApiResponse(mockJobs[index])
      }
      return mockApiError('Job not found')
    }
    return api.put(`/v1/jobs/${id}`, data)
  },
  delete: (id) => {
    if (USE_MOCK_API) {
      const index = mockJobs.findIndex(j => j.id === id)
      if (index !== -1) {
        mockJobs.splice(index, 1)
        return mockApiResponse({ success: true })
      }
      return mockApiError('Job not found')
    }
    return api.delete(`/v1/jobs/${id}`)
  },
}

export default api
