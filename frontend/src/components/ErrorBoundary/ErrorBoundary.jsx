import React from 'react'
import styled from 'styled-components'
import { FiAlertTriangle, FiRefreshCw, FiHome } from 'react-icons/fi'

const ErrorContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  padding: 40px 20px;
  text-align: center;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin: 20px;
`

const ErrorIcon = styled.div`
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff6b6b, #ee5a24);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
  
  svg {
    width: 40px;
    height: 40px;
    color: white;
  }
`

const ErrorTitle = styled.h2`
  font-size: 1.5rem;
  color: #2c3e50;
  margin: 0 0 12px 0;
`

const ErrorMessage = styled.p`
  color: #6c757d;
  font-size: 1rem;
  line-height: 1.5;
  margin: 0 0 24px 0;
  max-width: 500px;
`

const ErrorDetails = styled.details`
  margin: 20px 0;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e9ecef;
  max-width: 600px;
  width: 100%;
  
  summary {
    cursor: pointer;
    font-weight: 500;
    color: #495057;
    margin-bottom: 12px;
  }
  
  pre {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 0.85rem;
    margin: 0;
  }
`

const ActionButtons = styled.div`
  display: flex;
  gap: 12px;
  
  @media (max-width: 480px) {
    flex-direction: column;
    width: 100%;
    max-width: 300px;
  }
`

const ActionButton = styled.button`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &.primary {
    background: #007bff;
    color: white;
    
    &:hover {
      background: #0056b3;
      transform: translateY(-1px);
    }
  }
  
  &.secondary {
    background: #6c757d;
    color: white;
    
    &:hover {
      background: #545b62;
      transform: translateY(-1px);
    }
  }
`

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, error: null, errorInfo: null }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    })
    
    // Log error to console in development
    if (process.env.NODE_ENV === 'development') {
      console.error('ErrorBoundary caught an error:', error, errorInfo)
    }
    
    // Here you could also log to an error reporting service
    // logErrorToService(error, errorInfo)
  }

  handleReload = () => {
    window.location.reload()
  }

  handleGoHome = () => {
    window.location.href = '/'
  }

  render() {
    if (this.state.hasError) {
      return (
        <ErrorContainer>
          <ErrorIcon>
            <FiAlertTriangle />
          </ErrorIcon>
          
          <ErrorTitle>Something went wrong</ErrorTitle>
          
          <ErrorMessage>
            We're sorry, but something unexpected happened. The error has been logged 
            and our team will look into it. Please try refreshing the page or go back to the home page.
          </ErrorMessage>
          
          {process.env.NODE_ENV === 'development' && this.state.error && (
            <ErrorDetails>
              <summary>Error Details (Development Mode)</summary>
              <pre>
                {this.state.error.toString()}
                {this.state.errorInfo.componentStack}
              </pre>
            </ErrorDetails>
          )}
          
          <ActionButtons>
            <ActionButton className="primary" onClick={this.handleReload}>
              <FiRefreshCw />
              Reload Page
            </ActionButton>
            <ActionButton className="secondary" onClick={this.handleGoHome}>
              <FiHome />
              Go Home
            </ActionButton>
          </ActionButtons>
        </ErrorContainer>
      )
    }

    return this.props.children
  }
}

export default ErrorBoundary
