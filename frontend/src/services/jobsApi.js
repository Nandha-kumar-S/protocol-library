import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1';

export const jobsApi = {
  getAllJobs: () => axios.get(`${BASE_URL}/jobs/`),
  getJobById: (id) => axios.get(`${BASE_URL}/jobs/${id}/`),
  getJobSchemaById: (id) => axios.get(`${BASE_URL}/documents/${id}/USDM_JSON/`),
  updateJobStatus: (id, status) => axios.patch(`${BASE_URL}/jobs/${id}/`, { status }),
  exportToExcel: (id) => ({
    url: `${BASE_URL}/documents/export/${id}/INDIVIDUAL_SCHEMA`,
    method: 'GET',
    responseType: 'blob',
  }),
};

export const JobStatus = {
  STARTED: 'STARTED',
  PARSING: 'PARSING',
  PREPROCESSING: 'PREPROCESSING',
  MAP_SECTIONS_TO_SCHEMAS: 'MAP_SECTIONS_TO_SCHEMAS',
  CONTENT_EXTRACTION_PAUSED: 'CONTENT_EXTRACTION_PAUSED',
  MAP_CONTENT_TO_SCHEMAS: 'MAP_CONTENT_TO_SCHEMAS',
  CONNECT_SCHEMAS: 'CONNECT_SCHEMAS',
  LINK_SCHEMAS: 'LINK_SCHEMAS',
  FAILED: 'FAILED'
};
