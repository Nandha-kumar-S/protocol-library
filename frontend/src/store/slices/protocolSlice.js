import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { protocolAPI } from '../../services/api'

// Async thunks for API calls
export const fetchProtocols = createAsyncThunk(
  'protocols/fetchProtocols',
  async (_, { rejectWithValue }) => {
    try {
      const response = await protocolAPI.getAll()
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

export const createProtocol = createAsyncThunk(
  'protocols/createProtocol',
  async (protocolData, { rejectWithValue }) => {
    try {
      const response = await protocolAPI.create(protocolData)
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

export const updateProtocol = createAsyncThunk(
  'protocols/updateProtocol',
  async ({ id, data }, { rejectWithValue }) => {
    try {
      const response = await protocolAPI.update(id, data)
      return response.data
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

export const deleteProtocol = createAsyncThunk(
  'protocols/deleteProtocol',
  async (id, { rejectWithValue }) => {
    try {
      await protocolAPI.delete(id)
      return id
    } catch (error) {
      return rejectWithValue(error.response?.data || error.message)
    }
  }
)

const protocolSlice = createSlice({
  name: 'protocols',
  initialState: {
    items: [],
    selectedProtocol: null,
    loading: false,
    error: null,
    jsonEditorData: {},
  },
  reducers: {
    setSelectedProtocol: (state, action) => {
      state.selectedProtocol = action.payload
    },
    clearSelectedProtocol: (state) => {
      state.selectedProtocol = null
    },
    updateJsonEditorData: (state, action) => {
      state.jsonEditorData = action.payload
    },
    clearError: (state) => {
      state.error = null
    },
  },
  extraReducers: (builder) => {
    builder
      // Fetch protocols
      .addCase(fetchProtocols.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchProtocols.fulfilled, (state, action) => {
        state.loading = false
        state.items = action.payload
      })
      .addCase(fetchProtocols.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload
      })
      // Create protocol
      .addCase(createProtocol.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(createProtocol.fulfilled, (state, action) => {
        state.loading = false
        state.items.push(action.payload)
      })
      .addCase(createProtocol.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload
      })
      // Update protocol
      .addCase(updateProtocol.fulfilled, (state, action) => {
        const index = state.items.findIndex(item => item.id === action.payload.id)
        if (index !== -1) {
          state.items[index] = action.payload
        }
      })
      // Delete protocol
      .addCase(deleteProtocol.fulfilled, (state, action) => {
        state.items = state.items.filter(item => item.id !== action.payload)
        if (state.selectedProtocol?.id === action.payload) {
          state.selectedProtocol = null
        }
      })
  },
})

export const {
  setSelectedProtocol,
  clearSelectedProtocol,
  updateJsonEditorData,
  clearError,
} = protocolSlice.actions

export default protocolSlice.reducer
