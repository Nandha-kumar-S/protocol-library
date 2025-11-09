import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useToast } from '../../contexts/ToastContext';
import SectionView from './SectionView';
import TableModal from './TableModal';
import DeleteModal from './DeleteModal';
import { PageContainer } from './styles';
import { getJob, deleteJobSection, getJobDetails, approveJob, rejectJob } from '../../services/jobService';
import { removeObjectWithDeepCompare } from './utils';
import { FiArrowLeft, FiClock } from 'react-icons/fi';
import { Header, BackIconButton, JobDetailCard, JobInfo, JobTitle, JobMeta, MetaItem } from './styles';
import StatusBadge from '../../components/StatusBadge/StatusBadge';


const JobDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [job, setJob] = useState(null);
  const [jobDetails, setJobDetails] = useState(null);
  const [isApproving, setIsApproving] = useState(false);
  const [isRejecting, setIsRejecting] = useState(false);
  const [showTableModal, setShowTableModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [selectedSection, setSelectedSection] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [jsonResponse, setJsonResponse] = useState(null);
  // Get array of section keys for navigation
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const { showSuccess, showError } = useToast();
  const sectionKeys = Object.keys(job?.sections || {});

  const fetchJobDetails = useCallback(async () => {
    try {
      setIsLoading(true);
      setError(null);
      
      // Fetch job details for header
      const jobDetailsResponse = await getJobDetails(id);
      setJobDetails(jobDetailsResponse);

      // Fetch job content for sections
      const response = await getJob(id);
      setJsonResponse(response);

      if (!response || typeof response.json_value !== 'object') {
        throw new Error('Invalid response format');
      }

      // Transform the API response to match the UI needs
      const sections = {};
      Object.entries(response.json_value).forEach(([key, value]) => {
        if (Array.isArray(value) && value.length > 0) {
          const items = value
            .map(item => ({
              title: item.title || '',
              extracted_text: item.extracted_text || '',
              extracted_tables: Array.isArray(item.extracted_tables)
                ? item.extracted_tables.map(table => ({
                    columns: table.columns,
                    data: Array.isArray(table.data) ? table.data : []
                  }))
                : []
            }))
            .filter(item =>
              item.title ||
              item.extracted_text ||
              (item.extracted_tables && item.extracted_tables.length > 0)
            );
          
          if (items.length > 0) {
            sections[key] = {
              id: key,
              title: key,
              items
            };
          }
        }
      });

      setJob(prev => ({
        ...prev,
        sections,
        status: jobDetailsResponse?.status || prev?.status
      }));
    } catch (error) {
      console.error('Error fetching job details:', error);
      setError(error.message || 'Failed to load job details');
      showError(error.message || 'Failed to load job details');
    } finally {
      setIsLoading(false);
    }
  }, [id, showError]);

  // Initial data fetch
  useEffect(() => {
    fetchJobDetails();
  }, [fetchJobDetails]);

  // Handle keyboard navigation
  useEffect(() => {
    const handleKeyPress = (e) => {
      if (!job || showTableModal || showDeleteModal) return;

      let newIndex;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        newIndex = currentIndex + 1 >= sectionKeys.length ? currentIndex : currentIndex + 1;
      } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        newIndex = currentIndex - 1 < 0 ? 0 : currentIndex - 1;
      } else {
        return;
      }

      setCurrentIndex(newIndex);
      const section = job.sections[sectionKeys[newIndex]];
      setSelectedSection(section);
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [job, currentIndex, sectionKeys, showTableModal, showDeleteModal]);


  const handleDelete = async () => {
    if (!selectedSection) return;

    try {
      const updatedValue = removeObjectWithDeepCompare(jsonResponse, selectedSection);
      
      // Update the API
      await deleteJobSection(jobDetails.document_id, "EXTRACTED_CONTENT", null, updatedValue);
      
      // Fetch the latest job details to ensure UI is in sync
      await fetchJobDetails();
      
      // Reset UI state
      setSelectedSection(null);
      setCurrentIndex(0);
      setShowDeleteModal(false);
      
      showSuccess('Selected section deleted successfully');
    } catch (error) {
      console.error('Error deleting section:', error);
      showError('Failed to delete section. Please try again.');
    }
  };

  const handleApprove = async () => {
    setIsApproving(true);
    try {
      await approveJob(id);
      showSuccess('Job approved successfully!');
      // Refetch job details to update status
      const jobDetailsResponse = await getJobDetails(id);
      setJobDetails(jobDetailsResponse);
      setJob(prev => prev ? { ...prev, status: jobDetailsResponse?.status } : prev);
    } catch (error) {
      setError(error.message || 'Error approving job');
      showError(error.message || 'Error approving job');
    } finally {
      setIsApproving(false);
    }
  };

  const handleReject = async () => {
    setIsRejecting(true);
    try {
      await rejectJob(id);
      showSuccess('Job rejected successfully!');  
      // Refetch job details to update status
      const jobDetailsResponse = await getJobDetails(id);
      setJobDetails(jobDetailsResponse);
      setJob(prev => prev ? { ...prev, status: jobDetailsResponse?.status } : prev);
    } catch (error) {
      setError(error.message || 'Error rejecting job');
      showError(error.message || 'Error rejecting job');
    } finally {
      setIsRejecting(false);
    }
  };

  return (
    <PageContainer>
    <Header>
      <JobDetailCard>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '24px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '16px', flex: 1 }}>
            <BackIconButton onClick={() => navigate('/jobs')} title="Back to Jobs">
              <FiArrowLeft size={20} />
            </BackIconButton>
            <div style={{ flex: 1 }}>
              <JobInfo>
                <JobTitle>
                  {jobDetails?.title || 'Job Details'}
                  <StatusBadge status={jobDetails?.status || 'UNKNOWN'} />
                </JobTitle>
              </JobInfo>
              <JobMeta>
                <MetaItem>
                  <FiClock size={14} />
                  <span>This page allows you to review extracted documents and modify their sections.</span>
                </MetaItem>
              </JobMeta>
            </div>
          </div>
          {jobDetails?.status === 'CONTENT_EXTRACTION_PAUSED' && (
            <div style={{ display: 'flex', gap: '1rem', marginLeft: 'auto' }}>
              <button
                onClick={handleApprove}
                disabled={isApproving || isRejecting}
                style={{
                  padding: '12px 32px',
                  background: isApproving ? '#16a34a' : '#22c55e',
                  color: '#fff',
                  border: 'none',
                  borderRadius: '8px',
                  fontWeight: 600,
                  fontSize: '1rem',
                  boxShadow: isApproving ? '0 2px 8px rgba(34,197,94,0.15)' : '0 2px 8px rgba(34,197,94,0.10)',
                  cursor: isApproving || isRejecting ? 'not-allowed' : 'pointer',
                  opacity: isApproving ? 0.7 : 1,
                  transition: 'background 0.2s, box-shadow 0.2s'
                }}
              >
                {isApproving ? 'Approving...' : 'Approve'}
              </button>
              <button
                onClick={handleReject}
                disabled={isRejecting || isApproving}
                style={{
                  padding: '12px 32px',
                  background: isRejecting ? '#b91c1c' : '#ef4444',
                  color: '#fff',
                  border: 'none',
                  borderRadius: '8px',
                  fontWeight: 600,
                  fontSize: '1rem',
                  boxShadow: isRejecting ? '0 2px 8px rgba(239,68,68,0.15)' : '0 2px 8px rgba(239,68,68,0.10)',
                  cursor: isRejecting || isApproving ? 'not-allowed' : 'pointer',
                  opacity: isRejecting ? 0.7 : 1,
                  transition: 'background 0.2s, box-shadow 0.2s'
                }}
              >
                {isRejecting ? 'Rejecting...' : 'Reject'}
              </button>
            </div>
          )}
        </div>
      </JobDetailCard>
    </Header>

      <SectionView
        sections={job?.sections}
        currentSection={currentIndex}
        jobStatus={job?.status}
        onViewTable={(section) => {
          setSelectedSection(section);
          setShowTableModal(true);
        }}
        onDelete={(section) => {
          setSelectedSection(section);
          setShowDeleteModal(true);
        }}
      />

      {showTableModal && (
        <TableModal
          section={selectedSection}
          onClose={() => setShowTableModal(false)}
        />
      )}

      {showDeleteModal && (
        <DeleteModal
          section={selectedSection}
          onConfirm={handleDelete}
          onClose={() => setShowDeleteModal(false)}
        />
      )}
    </PageContainer>
  );
};

export default JobDetail;
