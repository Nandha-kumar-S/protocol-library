import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'
import { FiHome, FiArrowLeft } from 'react-icons/fi'

const NotFoundContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: 40px 20px;
`

const ErrorCode = styled.h1`
  font-size: 8rem;
  font-weight: 700;
  color: #e9ecef;
  margin: 0;
  line-height: 1;
  
  @media (max-width: 768px) {
    font-size: 6rem;
  }
`

const ErrorTitle = styled.h2`
  font-size: 2rem;
  color: #2c3e50;
  margin: 20px 0 10px 0;
  
  @media (max-width: 768px) {
    font-size: 1.5rem;
  }
`

const ErrorDescription = styled.p`
  font-size: 1.1rem;
  color: #6c757d;
  margin: 0 0 40px 0;
  max-width: 500px;
  line-height: 1.5;
`

const ActionButtons = styled.div`
  display: flex;
  gap: 16px;
  
  @media (max-width: 480px) {
    flex-direction: column;
    width: 100%;
    max-width: 300px;
  }
`

const ActionButton = styled(Link)`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
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

const NotFound = () => {
  return (
    <NotFoundContainer>
      <ErrorCode>404</ErrorCode>
      <ErrorTitle>Page Not Found</ErrorTitle>
      <ErrorDescription>
        The page you're looking for doesn't exist or has been moved. 
        Let's get you back on track.
      </ErrorDescription>
      <ActionButtons>
        <ActionButton to="/" className="primary">
          <FiHome />
          Go Home
        </ActionButton>
        <ActionButton to="/protocols" className="secondary">
          <FiArrowLeft />
          Back to Protocols
        </ActionButton>
      </ActionButtons>
    </NotFoundContainer>
  )
}

export default NotFound
