// Reject job by job id
export const rejectJob = async (jobId) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/jobs/${jobId}/REJECT`);
    return response.data;
  } catch (error) {
    console.error('Error rejecting job:', error);
    throw error;
  }
};
// Get job details by job id
export const getJobDetails = async (jobId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/jobs/${jobId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching job details:', error);
    throw error;
  }
};

// Approve job by job id
export const approveJob = async (jobId) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/jobs/${jobId}/APPROVE`);
    return response.data;
  } catch (error) {
    console.error('Error approving job:', error);
    throw error;
  }
};
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export const getJob = async (documentId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/documents/${documentId}/EXTRACTED_CONTENT`);
    return response.data;
  } catch (error) {
    console.error('Error fetching document:', error);
    throw error;
  }
};

export const deleteJobSection = async (documentId, jsonType, schemaName, updateJsonValue) => {
  try {
    const schemaQuery = schemaName ? `?schema_name=${schemaName}` : '';
    const response = await axios.put(`${API_BASE_URL}/documents/${documentId}/${jsonType}${schemaQuery}`, updateJsonValue);
    return response.data;
  } catch (error) {
    console.error('Error deleting section:', error);
    throw error;
  }
};
