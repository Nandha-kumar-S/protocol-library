import { store } from '../store/store'
import { fetchJobStatus, updateJobStatus, stopPolling } from '../store/slices/jobSlice'

class PollingService {
  constructor() {
    this.intervals = new Map()
  }

  startPolling(jobId, intervalMs = 5000) {
    // Don't start if already polling
    if (this.intervals.has(jobId)) {
      return
    }

    const intervalId = setInterval(async () => {
      try {
        const result = await store.dispatch(fetchJobStatus(jobId))
        const jobStatus = result.payload

        // Update job status in store
        store.dispatch(updateJobStatus({
          jobId,
          status: jobStatus.status
        }))

        // Stop polling if job is completed or failed
        if (jobStatus.status === 'completed' || jobStatus.status === 'failed') {
          this.stopPolling(jobId)
          store.dispatch(stopPolling(jobId))
        }
      } catch (error) {
        console.error(`Polling error for job ${jobId}:`, error)
        // Continue polling even on error, but could implement retry logic here
      }
    }, intervalMs)

    this.intervals.set(jobId, intervalId)
  }

  stopPolling(jobId) {
    const intervalId = this.intervals.get(jobId)
    if (intervalId) {
      clearInterval(intervalId)
      this.intervals.delete(jobId)
    }
  }

  stopAllPolling() {
    this.intervals.forEach((intervalId) => {
      clearInterval(intervalId)
    })
    this.intervals.clear()
  }

  isPolling(jobId) {
    return this.intervals.has(jobId)
  }

  getActivePollingJobs() {
    return Array.from(this.intervals.keys())
  }
}

export const pollingService = new PollingService()

// Auto-start polling for in-progress jobs when the service is initialized
export const initializePolling = () => {
  const state = store.getState()
  const inProgressJobs = state.jobs.inProgressJobs

  inProgressJobs.forEach(job => {
    pollingService.startPolling(job.id)
  })
}

export default pollingService
