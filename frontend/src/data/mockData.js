// Mock data for testing the Protocol Library application

export const mockProtocols = [
  {
    id: '1',
    title: 'Clinical Trial Protocol v2.1',
    description: 'Comprehensive protocol for phase II clinical trial including patient recruitment, data collection, and analysis procedures.',
    content: {
      version: '2.1',
      phases: ['screening', 'baseline', 'treatment', 'followup'],
      endpoints: {
        primary: 'Overall survival',
        secondary: ['Progression-free survival', 'Quality of life']
      },
      inclusion_criteria: [
        'Age 18-75 years',
        'Confirmed diagnosis',
        'ECOG performance status 0-2'
      ]
    },
    createdAt: '2024-01-15T10:30:00Z',
    updatedAt: '2024-02-20T14:45:00Z'
  },
  {
    id: '2',
    title: 'Data Collection Protocol',
    description: 'Standard operating procedure for collecting and managing research data across multiple sites.',
    content: {
      data_types: ['demographics', 'clinical', 'laboratory', 'imaging'],
      collection_schedule: {
        baseline: 'Day 0',
        week_4: 'Day 28',
        week_12: 'Day 84'
      },
      quality_control: {
        double_entry: true,
        range_checks: true,
        consistency_checks: true
      }
    },
    createdAt: '2024-01-10T09:15:00Z',
    updatedAt: '2024-02-15T11:20:00Z'
  },
  {
    id: '3',
    title: 'Biomarker Analysis Protocol',
    description: 'Laboratory protocol for biomarker identification and validation in clinical samples.',
    content: {
      sample_types: ['blood', 'tissue', 'urine'],
      assays: ['ELISA', 'PCR', 'Western blot'],
      storage_conditions: {
        temperature: '-80°C',
        duration: '5 years',
        aliquot_size: '500μL'
      }
    },
    createdAt: '2024-01-20T16:00:00Z',
    updatedAt: '2024-02-25T10:30:00Z'
  }
]

export const mockStudies = [
  {
    id: '1',
    title: 'Cardiovascular Health Study',
    description: 'Long-term observational study investigating cardiovascular risk factors in adults aged 40-70.',
    participants: 1250,
    startDate: '2024-01-01',
    endDate: '2026-12-31',
    status: 'active',
    protocols: ['1', '2'],
    pages: ['1', '2', '3'],
    createdAt: '2023-12-01T08:00:00Z',
    updatedAt: '2024-02-28T15:30:00Z'
  },
  {
    id: '2',
    title: 'Diabetes Prevention Trial',
    description: 'Randomized controlled trial evaluating lifestyle interventions for diabetes prevention.',
    participants: 800,
    startDate: '2024-02-15',
    endDate: '2025-08-15',
    status: 'active',
    protocols: ['1', '3'],
    pages: ['4', '5'],
    createdAt: '2024-01-15T10:00:00Z',
    updatedAt: '2024-02-28T12:15:00Z'
  },
  {
    id: '3',
    title: 'Mental Health Longitudinal Study',
    description: 'Prospective cohort study examining mental health outcomes over 10 years.',
    participants: 2000,
    startDate: '2023-06-01',
    endDate: '2033-05-31',
    status: 'active',
    protocols: ['2'],
    pages: ['6', '7', '8', '9'],
    createdAt: '2023-05-01T09:30:00Z',
    updatedAt: '2024-02-20T14:00:00Z'
  }
]

export const mockJobs = [
  {
    id: '1',
    title: 'Data Export - Cardiovascular Study',
    description: 'Exporting participant data for statistical analysis',
    status: 'completed',
    progress: 100,
    createdAt: '2024-02-28T09:00:00Z',
    completedAt: '2024-02-28T09:15:00Z'
  },
  {
    id: '2',
    title: 'Report Generation - Q1 2024',
    description: 'Generating quarterly progress report for all active studies',
    status: 'in_progress',
    progress: 65,
    createdAt: '2024-02-28T10:30:00Z'
  },
  {
    id: '3',
    title: 'Database Backup',
    description: 'Weekly automated backup of research database',
    status: 'in_progress',
    progress: 25,
    createdAt: '2024-02-28T11:00:00Z'
  },
  {
    id: '4',
    title: 'Data Validation - Diabetes Trial',
    description: 'Running data quality checks on recent entries',
    status: 'failed',
    progress: 45,
    createdAt: '2024-02-28T08:00:00Z',
    failedAt: '2024-02-28T08:30:00Z'
  },
  {
    id: '5',
    title: 'Statistical Analysis - Biomarkers',
    description: 'Performing correlation analysis on biomarker data',
    status: 'pending',
    progress: 0,
    createdAt: '2024-02-28T12:00:00Z'
  }
]

export const mockRelatedPages = {
  '1': [ // Cardiovascular Health Study
    {
      id: '1',
      title: 'Participant Enrollment Form',
      description: 'Initial enrollment and consent form for study participants',
      type: 'form',
      updatedAt: '2024-02-25T10:00:00Z'
    },
    {
      id: '2',
      title: 'Baseline Assessment',
      description: 'Comprehensive baseline health assessment including vitals and medical history',
      type: 'assessment',
      updatedAt: '2024-02-26T14:30:00Z'
    },
    {
      id: '3',
      title: 'Follow-up Questionnaire',
      description: 'Monthly follow-up questionnaire for tracking health status changes',
      type: 'questionnaire',
      updatedAt: '2024-02-27T09:15:00Z'
    }
  ],
  '2': [ // Diabetes Prevention Trial
    {
      id: '4',
      title: 'Lifestyle Intervention Tracking',
      description: 'Daily tracking form for diet and exercise interventions',
      type: 'tracking',
      updatedAt: '2024-02-28T11:00:00Z'
    },
    {
      id: '5',
      title: 'Glucose Monitoring Log',
      description: 'Weekly glucose level monitoring and recording form',
      type: 'monitoring',
      updatedAt: '2024-02-28T13:45:00Z'
    }
  ],
  '3': [ // Mental Health Longitudinal Study
    {
      id: '6',
      title: 'Mental Health Screening',
      description: 'Initial mental health screening questionnaire using validated instruments',
      type: 'screening',
      updatedAt: '2024-02-20T16:00:00Z'
    },
    {
      id: '7',
      title: 'Stress Assessment Scale',
      description: 'Quarterly stress level assessment using standardized scales',
      type: 'assessment',
      updatedAt: '2024-02-22T10:30:00Z'
    },
    {
      id: '8',
      title: 'Life Events Questionnaire',
      description: 'Annual questionnaire documenting major life events and changes',
      type: 'questionnaire',
      updatedAt: '2024-02-24T15:20:00Z'
    },
    {
      id: '9',
      title: 'Treatment Response Form',
      description: 'Form for documenting response to mental health interventions',
      type: 'form',
      updatedAt: '2024-02-26T12:10:00Z'
    }
  ]
}

// Helper functions for mock API simulation
export const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms))

export const mockApiResponse = (data, delayMs = 500) => {
  return delay(delayMs).then(() => ({
    data,
    status: 200,
    statusText: 'OK'
  }))
}

export const mockApiError = (message = 'API Error', delayMs = 500) => {
  return delay(delayMs).then(() => {
    throw new Error(message)
  })
}
