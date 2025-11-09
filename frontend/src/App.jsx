import React, { useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'
import styled from 'styled-components'
import Toast from './components/Toast/Toast'
import { initializePolling } from './services/polling'
import Layout from './components/Layout/Layout'
import ErrorBoundary from './components/ErrorBoundary/ErrorBoundary'
import { ToastProvider } from './contexts/ToastContext'
import UploadPDFs from './pages/UploadPDFs'
import Jobs from './pages/Jobs'
import InProgressJobs from './pages/InProgressJobs'
import JobDetail from './pages/jobDetail'
import SchemaDetail from './pages/SchemaDetail'
import NotFound from './pages/NotFound'
import useKeyboardShortcuts from './hooks/useKeyboardShortcuts'
import USDMViewer from './pages/USDMViewer/USDMViewer'

const AppContainer = styled.div`
  min-height: 100vh;
  background-color: #f8f9fa;
`

function App() {
  
  // Initialize keyboard shortcuts
  useKeyboardShortcuts()

  useEffect(() => {
    // Initialize polling service for in-progress jobs
    initializePolling()
    
    // Cleanup polling on unmount
    return () => {
      // pollingService will be cleaned up automatically
    }
  }, [])

  return (
    <ErrorBoundary>
      <ToastProvider>
        <AppContainer>
          <Layout>
            <Routes>
              <Route path="/" element={<UploadPDFs />} />
              <Route path="/upload" element={<UploadPDFs />} />
              <Route path="/jobs" element={<Jobs />} />
              <Route path="/jobs/in-progress" element={<InProgressJobs />} />
              <Route path="/job-detail/:id" element={<JobDetail />} />
              <Route path="/schema-detail/:id" element={<SchemaDetail />} />
              <Route path="/viewer/:id" element={<USDMViewer />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </Layout>
          <Toast />
        </AppContainer>
      </ToastProvider>
    </ErrorBoundary>
  )
}

export default App
