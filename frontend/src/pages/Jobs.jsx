import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import styled from 'styled-components'
import { FiChevronDown, FiChevronRight, FiEye, FiCheck, FiAlertCircle, FiClock } from 'react-icons/fi'
import { jobAPI } from '../services/api'
import { STATUS_MAPPING } from '../utils/statusUtils'
import StatusBadge from '../components/StatusBadge/StatusBadge'
import {
  STATUS_STAGES,
  getDisplayStatus,
  getCurrentStageIndex,
  getProgressPercentage,
  formatDate
} from '../utils/statusUtils'

const PageContainer = styled.div`
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
`

const PageTitle = styled.h1`
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 30px;
  font-weight: 600;
`

const JobsTable = styled.div`
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-top: 20px;
`

const FilterContainer = styled.div`
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
  flex-wrap: wrap;
`

const FilterInput = styled.input`
  padding: 8px 12px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 14px;
  min-width: 200px;
  
  &:focus {
    outline: none;
    border-color: #80bdff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
  }
`

const FilterSelect = styled.select`
  padding: 8px 12px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 14px;
  min-width: 200px;
  background-color: white;
  cursor: pointer;
  
  &:focus {
    outline: none;
    border-color: #80bdff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
  }
`

const TableHeader = styled.div`
  background: #f8f9fa;
  padding: 8px 12px;
  display: grid;
  grid-template-columns: 50px minmax(120px, 1fr) 180px 180px minmax(250px, 1fr) minmax(180px, 1fr);
  gap: 8px;
  font-weight: 600;
  color: #495057;
  font-size: 0.9rem;
  border-bottom: 1px solid #dee2e6;
`

const TableRow = styled.div`
  border-bottom: 1px solid #f1f3f4;
  transition: background 0.2s ease;
  
  &:hover {
    background: #f8f9fa;
  }
  
  &:last-child {
    border-bottom: none;
  }
`

const RowContent = styled.div`
  padding: 8px 12px;
  display: grid;
  grid-template-columns: 50px minmax(120px, 1fr) 180px 180px minmax(250px, 1fr) minmax(180px, 1fr);
  gap: 8px;
  align-items: center;
`

const ExpandedContent = styled.div`
  padding: 8px 12px;
  background: #f8f9fa;
  border-top: 1px solid #dee2e6;
`

const StatusCell = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
`

const ExpandIcon = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  color: #6c757d;
  transition: transform 0.2s ease;
  
  &:hover {
    color: #495057;
  }
`

const JobName = styled.div`
  font-weight: 500;
  color: #2c3e50;
`

const DateText = styled.div`
  color: #6c757d;
  font-size: 0.9rem;
`

const ActionButtons = styled.div`
  display: flex;
  gap: 8px;
  align-items: center;
`

const ActionButton = styled.button`
  background: ${props => props.variant === 'primary' ? props.color || '#007bff' : 'none'};
  border: 1px solid ${props => props.color || '#dee2e6'};
  border-radius: 6px;
  padding: 8px 12px;
  cursor: pointer;
  color: ${props => props.variant === 'primary' ? 'white' : props.color || '#6c757d'};
  transition: all 0.2s ease;
  font-size: 0.85rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-width: ${props => props.minWidth || '140px'};
  white-space: nowrap;
  text-align: center;
  
  &:hover {
    background: ${props => props.variant === 'primary' ?
    `color-mix(in srgb, ${props.color || '#007bff'} 85%, black)` :
    props.color ? `${props.color}15` : '#e9ecef'
  };
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
  }
  
  svg {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
  }
`

const RequiresAttentionRow = styled(RowContent)`
  background: linear-gradient(90deg, #fff3cd 0%, #ffffff 100%);
  border-left: 4px solid #ffc107;
  
  &:hover {
    background: linear-gradient(90deg, #ffeaa7 0%, #f8f9fa 100%);
  }
`

const AttentionBadge = styled.div`
  background: #ffc107;
  color: #856404;
  font-size: 0.7rem;
  padding: 2px 6px;
  border-radius: 10px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 2px;
  
  svg {
    width: 10px;
    height: 10px;
  }
`

const StatusRoadmap = styled.div`
  margin-top: 16px;
`

const RoadmapTitle = styled.h4`
  margin: 0 0 20px 0;
  color: #2c3e50;
  font-size: 1.1rem;
  font-weight: 600;
`

const ProgressContainer = styled.div`
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px 0;
`

const ProgressLine = styled.div`
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 2px;
  background: #dee2e6;
  transform: translateY(-50%);
  z-index: 1;
`

const ProgressFill = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: #28a745;
  transition: width 0.3s ease;
  z-index: 2;
`

const StageItem = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 3;
  flex: 1;
`

const StageCircle = styled.div`
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: ${props => props.completed ? props.color : '#dee2e6'};
  border: 3px solid white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
  
  ${props => props.current && `
    animation: pulse 2s infinite;
    box-shadow: 0 0 0 4px ${props.color}20;
  `}
  
  @keyframes pulse {
    0% {
      box-shadow: 0 0 0 0 ${props => props.color}40;
    }
    70% {
      box-shadow: 0 0 0 6px ${props => props.color}00;
    }
    100% {
      box-shadow: 0 0 0 0 ${props => props.color}00;
    }
  }
`

const StageLabel = styled.div`
  font-size: 0.8rem;
  color: ${props => props.completed ? '#2c3e50' : '#6c757d'};
  text-align: center;
  font-weight: ${props => props.current ? '600' : '400'};
  max-width: 100px;
  line-height: 1.2;
`

const LoadingSpinner = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  color: #6c757d;
`

const ErrorMessage = styled.div`
  text-align: center;
  padding: 40px;
  color: #dc3545;
  background: #f8d7da;
  border-radius: 8px;
  margin: 20px 0;
`

const Jobs = () => {
  const [jobs, setJobs] = useState([])
  const [filteredJobs, setFilteredJobs] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [expandedJobId, setExpandedJobId] = useState(null)
  const [statusFilter, setStatusFilter] = useState('')
  const [expandedRow, setExpandedRow] = useState(null)
  const navigate = useNavigate()

  // Toggle row expansion
  const toggleRowExpansion = (jobId) => {
    setExpandedRow(expandedRow === jobId ? null : jobId)
  }

  // Navigate to job detail
  const redirectToJobDetail = (jobId) => {
    navigate(`/job-detail/${jobId}`)
  }

  // Apply status filter to jobs using STATUS_MAPPING
  useEffect(() => {
    if (jobs.length > 0) {
      const filtered = statusFilter
        ? jobs.filter(job => {
          const mappedStatus = STATUS_MAPPING[job.status] || job.status;
          return mappedStatus === statusFilter;
        })
        : [...jobs]; // Create a new array to trigger re-render
      setFilteredJobs(filtered);
    } else {
      setFilteredJobs([]);
    }
  }, [jobs, statusFilter]);

  // Handle status filter change
  const handleStatusChange = (e) => {
    setStatusFilter(e.target.value)
  }

  // Clear status filter
  const clearFilter = () => {
    setStatusFilter('')
  }

  // Fetch jobs from API
  const fetchJobs = async () => {
    setLoading(true)
    try {
      const response = await jobAPI.getAll()
      if (response.data) {
        setJobs(response.data || [])
        setError(null)
      } else {
        throw new Error('Invalid response format from server')
      }
    } catch (err) {
      console.error('Error fetching jobs:', err)
      setError(err.message || 'Failed to fetch jobs')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchJobs()

    // Poll for updates every 30 seconds
    const interval = setInterval(fetchJobs, 30000)

    return () => clearInterval(interval)
  }, [])

  // Check if job requires user attention
  const requiresUserAttention = (status) => {
    return ['CONTENT_EXTRACTION_PAUSED'].includes(status)
  }

  // Get action buttons based on job status
  const getActionButtons = (job) => {
    const buttons = []
    // Status-specific action buttons
    if (job.status === 'CONTENT_EXTRACTION_PAUSED') {
      buttons.unshift(
        <ActionButton
          key="approve-extraction"
          variant="primary"
          color="#3b82f6"
          onClick={() => navigate(`/job-detail/${job.id}`)}
          title="Review and approve extracted content"
          minWidth="140px"
        >
          <FiCheck />
          Review required
        </ActionButton>
      )
    } else if (job.status === 'COMPLETED') {
      buttons.unshift(
        <ActionButton
          key="view-schema"
          variant="primary"
          color="#10b981"
          onClick={() => navigate(`/viewer/${job.id}`)}
          title="View extracted schema"
          minWidth="140px"
        >
          <FiEye />
          Check Result
        </ActionButton>
      )
    } else {
      buttons.unshift(
        <ActionButton
          key="processing"
          variant="primary"
          color="#6c757d"
          title="Job is being processed"
          minWidth="140px"
        >
          <FiClock />
          Processing
        </ActionButton>
      )
    }
    return buttons
  }

  // Get unique status display values from STATUS_MAPPING
  const statusOptions = [...new Set(Object.values(STATUS_MAPPING))];

  // Get unique statuses from jobs (mapped to display values)
  const jobStatuses = [...new Set(
    jobs.map(job => STATUS_MAPPING[job.status] || job.status)
  )];

  // Combine and deduplicate statuses
  const allStatuses = [...new Set([...statusOptions, ...jobStatuses])];
  const displayJobs = filteredJobs.length > 0 || statusFilter ? filteredJobs : jobs

  if (loading) {

    return (
      <PageContainer>
        <LoadingSpinner>Loading jobs...</LoadingSpinner>
      </PageContainer>
    )
  }

  if (error) {
    return (
      <PageContainer>
        <PageTitle>Jobs</PageTitle>
        <ErrorMessage>
          Error loading jobs: {error}
        </ErrorMessage>
      </PageContainer>
    )
  }

  return (
    <PageContainer>

      {/* Status Filter */}
      <FilterContainer>
        <div>
          <label htmlFor="status" style={{ display: 'block', marginBottom: '4px', fontSize: '14px', fontWeight: '500' }}>
            Filter by Status
          </label>
          <FilterSelect
            id="status"
            value={statusFilter}
            onChange={handleStatusChange}
          >
            <option value="">All Statuses</option>
            {allStatuses.map(status => (
              <option key={status} value={status}>
                {status}
              </option>
            ))}
          </FilterSelect>
        </div>

        {statusFilter && (
          <button
            onClick={clearFilter}
            style={{
              alignSelf: 'flex-end',
              padding: '8px 16px',
              background: 'transparent',
              border: '1px solid #dc3545',
              color: '#dc3545',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '14px',
              marginLeft: '16px',
              display: 'flex',
              alignItems: 'center',
              gap: '6px'
            }}
          >
            Clear Filter
          </button>
        )}
      </FilterContainer>
      <JobsTable>
        <TableHeader>
          <div>ID</div>
          <div>Name</div>
          <div>Created Date</div>
          <div>Last Updated</div>
          <div>Status</div>
          <div>Actions</div>
        </TableHeader>

        {displayJobs.length === 0 ? (
          <div style={{ gridColumn: '1 / -1', textAlign: 'center', padding: '20px', color: '#6c757d' }}>
            {statusFilter ? 'No jobs found with the selected status' : 'No jobs found'}
          </div>
        ) : (
          displayJobs.map((job) => {
            const needsAttention = requiresUserAttention(job.status)
            const RowComponent = needsAttention ? RequiresAttentionRow : RowContent
            const displayStatus = getDisplayStatus(job.status)
            return (
              <TableRow key={job.id}>
                <RowComponent>
                  <JobName>{job.id}</JobName>
                  <JobName>{job.name || job.document_name || 'Immediate Job'}</JobName>
                  <DateText>{formatDate(job.created_at)}</DateText>
                  <DateText>{formatDate(job.updated_at)}</DateText>
                  <StatusCell onClick={() => toggleRowExpansion(job.id)}>
                    <StatusBadge status={displayStatus} />
                    <ExpandIcon>
                      {expandedRow === job.id ? <FiChevronDown /> : <FiChevronRight />}
                    </ExpandIcon>
                  </StatusCell>
                  <ActionButtons>
                    {getActionButtons(job)}
                  </ActionButtons>
                </RowComponent>

                {expandedRow === job.id && (
                  <ExpandedContent>
                    <StatusRoadmap>
                      <RoadmapTitle>Processing Status</RoadmapTitle>
                      <ProgressContainer>
                        <ProgressLine>
                          {(() => {
                            // Filtered stages for progress calculation
                            const filteredStages = (job.status === 'FAILED'
                              ? STATUS_STAGES.filter(stage => stage.key !== 'Completed')
                              : STATUS_STAGES.filter(stage => stage.key !== 'Failed')
                            );
                            // Use display status for index
                            const statusForIndex = job.status === 'FAILED' ? job.status : (job.status || 'COMPLETED');
                            const displayStatus = getDisplayStatus(statusForIndex);
                            const currentIndex = filteredStages.findIndex(stage => stage.key === displayStatus);
                            // If status is not found, fill 0%
                            let percent = 0;
                            if (currentIndex === -1) {
                              percent = 0;
                            } else {
                              percent = ((currentIndex + 1) / filteredStages.length) * 100;
                            }
                            // Always fill 100% for completed/failed
                            if (displayStatus === 'Completed' || displayStatus === 'Failed') {
                              percent = 100;
                            }
                            return <ProgressFill style={{ width: `${percent}%` }} />;
                          })()}
                        </ProgressLine>
                        {(job.status === 'FAILED'
                          ? STATUS_STAGES.filter(stage => stage.key !== 'Completed')
                          : STATUS_STAGES.filter(stage => stage.key !== 'Failed')
                        ).map((stage, index, arr) => {
                          // If status is not Failed, default to Completed
                          const statusForIndex = job.status === 'FAILED' ? job.status : (job.status || 'COMPLETED');
                          const currentIndex = getCurrentStageIndex(statusForIndex);
                          const isCompleted = index <= currentIndex;
                          const isCurrent = index === currentIndex;
                          return (
                            <StageItem key={stage.key}>
                              <StageCircle
                                completed={isCompleted}
                                current={isCurrent}
                                color={stage.color}
                              />
                              <StageLabel completed={isCompleted} current={isCurrent}>
                                {stage.label}
                              </StageLabel>
                            </StageItem>
                          );
                        })}
                      </ProgressContainer>

                      {needsAttention && (
                        <div style={{
                          marginTop: '20px',
                          padding: '16px',
                          background: '#fff3cd',
                          border: '1px solid #ffeaa7',
                          borderRadius: '8px',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '12px'
                        }}>
                          <FiAlertCircle style={{ color: '#856404', width: '20px', height: '20px' }} />
                          <div>
                            <strong style={{ color: '#856404' }}>User Action Required</strong>
                            <p style={{ margin: '4px 0 0 0', color: '#856404', fontSize: '0.9rem' }}>
                              {job.status === 'CONTENT_EXTRACTION_PAUSED'
                                ? 'Please review the extracted content and approve to continue processing.'
                                : 'Please review the mapping and approve to complete the job.'
                              }
                            </p>
                          </div>
                        </div>
                      )}
                    </StatusRoadmap>
                  </ExpandedContent>
                )}
              </TableRow>
            )
          }))}

        {displayJobs.length === 0 && jobs.length > 0 && (
          <RowContent>
            <div style={{ gridColumn: '1 / -1', textAlign: 'center', color: '#6c757d', padding: '40px' }}>
              No jobs match your filter criteria
            </div>
          </RowContent>
        )}
      </JobsTable>
    </PageContainer>
  )
}

export default Jobs
