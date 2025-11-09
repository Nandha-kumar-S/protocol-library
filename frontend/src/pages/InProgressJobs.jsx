import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import styled from 'styled-components'
import { FiClock, FiExternalLink, FiGrid } from 'react-icons/fi'
import { jobAPI } from '../services/api'
import StatusBadge from '../components/StatusBadge/StatusBadge'

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

const JobsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
`

const JobCard = styled.div`
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 24px;
  transition: transform 0.2s ease;
  position: relative;
  
  &:hover {
    transform: translateY(-2px);
  }
`

const DocumentId = styled.span`
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 0.8rem;
  color: #6c757d;
`

const JobHeader = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
`

const JobTitle = styled.h3`
  margin: 0;
  font-size: 1.2rem;
  color: #2c3e50;
  font-weight: 600;
`

const JobStatus = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  background: #fff3cd;
  color: #856404;
`

const JobInfo = styled.div`
  margin-bottom: 16px;
`

const JobDetail = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 0.9rem;
  
  .label {
    color: #6c757d;
  }
  
  .value {
    color: #2c3e50;
    font-weight: 500;
  }
`

const ProgressBar = styled.div`
  width: 100%;
  height: 8px;
  background: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 16px;
`

const ProgressFill = styled.div`
  height: 100%;
  background: linear-gradient(90deg, #007bff, #0056b3);
  width: ${props => props.progress}%;
  transition: width 0.3s ease;
`

const JobActions = styled.div`
  display: flex;
  gap: 8px;
`

const ActionButton = styled.button`
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
  font-size: 0.8rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
  
  &.primary {
    background: #007bff;
    color: white;
    
    &:hover {
      background: #0056b3;
    }
  }
`

const EmptyState = styled.div`
  text-align: center;
  padding: 60px 20px;
  color: #6c757d;
  
  .icon {
    font-size: 3rem;
    margin-bottom: 20px;
  }
  
  .title {
    font-size: 1.2rem;
    margin-bottom: 10px;
    color: #495057;
  }
  
  .subtitle {
    font-size: 0.9rem;
  }
`

const InProgressJobs = () => {
  const navigate = useNavigate()
  const [jobs, setJobs] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const formatTime = (timeString) => {
    const date = new Date(timeString)
    return date.toLocaleTimeString('en-US', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const getElapsedTime = (startTime) => {
    const start = new Date(startTime)
    const now = new Date()
    const diff = Math.floor((now - start) / 1000 / 60) // minutes
    
    if (diff < 60) {
      return `${diff}m`
    } else {
      const hours = Math.floor(diff / 60)
      const minutes = diff % 60
      return `${hours}h ${minutes}m`
    }
  }

  const redirectToJobDetail = (jobId) => {
    // Navigate to the job detail page based on the screenshot wireframe
    navigate(`/job-detail/${jobId}`)
  }

  // Fetch in-progress jobs from API
  const fetchInProgressJobs = async () => {
    setLoading(true)
    const { data, error } = await jobAPI.getInProgress()
    setJobs(data)
    setError(error)
    setLoading(false)
  }

  useEffect(() => {
    fetchInProgressJobs()

    // Poll for updates every 5 seconds
    const interval = setInterval(() => {
      fetchInProgressJobs()
    }, 5000)

    return () => clearInterval(interval)
  }, [])

  return (
    <PageContainer>
      <PageTitle>In Progress Jobs</PageTitle>
      
      {jobs.length === 0 ? (
        <EmptyState>
          <div className="icon">
            <FiClock />
          </div>
          <div className="title">No jobs in progress</div>
          <div className="subtitle">All jobs have been completed or stopped</div>
        </EmptyState>
      ) : (
        <JobsGrid>
          {jobs.map(job => (
            <JobCard key={job.id}>
              <DocumentId>Document ID: {job.document_id}</DocumentId>
              <JobHeader>
                <JobTitle>Job #{job.id}</JobTitle>
                <StatusBadge status={job.status} />
              </JobHeader>
              
              <JobInfo>
                <JobDetail>
                  <span className="label">Created:</span>
                  <span className="value">{new Date(job.created_at).toLocaleString()}</span>
                </JobDetail>
                <JobDetail>
                  <span className="label">Last Updated:</span>
                  <span className="value">{new Date(job.updated_at).toLocaleString()}</span>
                </JobDetail>
                <JobDetail>
                  <span className="label">Elapsed:</span>
                  <span className="value">{getElapsedTime(job.created_at)}</span>
                </JobDetail>
              </JobInfo>
              
              <ProgressBar>
                <ProgressFill progress={job.progress} />
              </ProgressBar>
              
              <JobActions>
                <ActionButton className="primary" onClick={() => redirectToJobDetail(job.id)}>
                  <FiExternalLink />
                  View Details
                </ActionButton>
                <ActionButton 
                  className="secondary" 
                  onClick={() => navigate(`/schema/${job.id}`)}
                  style={{ marginLeft: '10px' }}
                >
                  <FiGrid />
                  Schema View
                </ActionButton>
              </JobActions>
            </JobCard>
          ))}
        </JobsGrid>
      )}
    </PageContainer>
  )
}

export default InProgressJobs
