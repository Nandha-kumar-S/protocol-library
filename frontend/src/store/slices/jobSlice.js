import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { jobAPI } from '../../services/api'

// Async thunks for API calls
export const fetchJobs = createAsyncThunk(
  'jobs/fetchJobs',
  async (_, { rejectWithValue }) => {
    try {
      const response = await jobAPI.getAll()
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

export const fetchJobStatus = createAsyncThunk(
  'jobs/fetchJobStatus',
  async (jobId, { rejectWithValue }) => {
    try {
      const response = await jobAPI.getStatus(jobId)
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

export const createJob = createAsyncThunk(
  'jobs/createJob',
  async (jobData, { rejectWithValue }) => {
    try {
      const response = await jobAPI.create(jobData)
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

const jobSlice = createSlice({
  name: 'jobs',
  initialState: {
    items: [],
    inProgressJobs: [],
    pollingIntervals: {},
    loading: false,
    error: null,
  },
  reducers: {
    startPolling: (state, action) => {
      const jobId = action.payload
      if (!state.pollingIntervals[jobId]) {
        state.pollingIntervals[jobId] = true
      }
    },
    stopPolling: (state, action) => {
      const jobId = action.payload
      delete state.pollingIntervals[jobId]
    },
    updateJobStatus: (state, action) => {
      const { jobId, status } = action.payload
      const jobIndex = state.items.findIndex(job => job.id === jobId)
      if (jobIndex !== -1) {
        state.items[jobIndex].status = status
      }
      
      // Update in-progress jobs list
      if (status === 'in_progress') {
        if (!state.inProgressJobs.find(job => job.id === jobId)) {
          const job = state.items.find(job => job.id === jobId)
          if (job) {
            state.inProgressJobs.push(job)
          }
        }
      } else {
        state.inProgressJobs = state.inProgressJobs.filter(job => job.id !== jobId)
      }
    },
    clearError: (state) => {
      state.error = null
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch jobs
      .addCase(fetchJobs.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchJobs.fulfilled, (state, action) => {
        state.loading = false
        state.items = action.payload
        // Update in-progress jobs
        state.inProgressJobs = action.payload.filter(job => job.status === 'in_progress')
      })
      .addCase(fetchJobs.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload
      })
      // Fetch job status
      .addCase(fetchJobStatus.fulfilled, (state, action) => {
        const { id, status } = action.payload
        const jobIndex = state.items.findIndex(job => job.id === id)
        if (jobIndex !== -1) {
          state.items[jobIndex] = action.payload
        }
      })
      // Create job
      .addCase(createJob.fulfilled, (state, action) => {
        state.items.push(action.payload)
        if (action.payload.status === 'in_progress') {
          state.inProgressJobs.push(action.payload)
        }
      })
  },
})

export const {
  startPolling,
  stopPolling,
  updateJobStatus,
  clearError,
} = jobSlice.actions

export default jobSlice.reducer
