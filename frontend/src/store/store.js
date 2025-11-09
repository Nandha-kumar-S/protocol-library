import { configureStore } from '@reduxjs/toolkit'
import protocolReducer from './slices/protocolSlice'

import jobReducer from './slices/jobSlice'

export const store = configureStore({
  reducer: {
    protocols: protocolReducer,

    jobs: jobReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST'],
      },
    }),
})
