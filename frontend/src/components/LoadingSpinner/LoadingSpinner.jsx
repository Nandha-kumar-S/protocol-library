import React from 'react'
import styled, { keyframes } from 'styled-components'

const spin = keyframes`
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
`

const pulse = keyframes`
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
`

const LoadingContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: ${props => props.size === 'large' ? '60px 20px' : '40px 20px'};
  min-height: ${props => props.fullHeight ? '400px' : 'auto'};
`

const Spinner = styled.div`
  width: ${props => {
    switch (props.size) {
      case 'small': return '24px'
      case 'large': return '60px'
      default: return '40px'
    }
  }};
  height: ${props => {
    switch (props.size) {
      case 'small': return '24px'
      case 'large': return '60px'
      default: return '40px'
    }
  }};
  border: ${props => {
    const width = props.size === 'small' ? '2px' : props.size === 'large' ? '4px' : '3px'
    return `${width} solid #f3f3f3`
  }};
  border-top: ${props => {
    const width = props.size === 'small' ? '2px' : props.size === 'large' ? '4px' : '3px'
    return `${width} solid #007bff`
  }};
  border-radius: 50%;
  animation: ${spin} 1s linear infinite;
  margin-bottom: ${props => props.showText ? '16px' : '0'};
`

const LoadingText = styled.p`
  color: #6c757d;
  font-size: ${props => props.size === 'large' ? '1.1rem' : '0.9rem'};
  margin: 0;
  animation: ${pulse} 1.5s ease-in-out infinite;
`

const LoadingSpinner = ({ 
  size = 'medium', // 'small', 'medium', 'large'
  text = 'Loading...', 
  showText = true,
  fullHeight = false 
}) => {
  return (
    <LoadingContainer size={size} fullHeight={fullHeight}>
      <Spinner size={size} showText={showText} />
      {showText && <LoadingText size={size}>{text}</LoadingText>}
    </LoadingContainer>
  )
}

export default LoadingSpinner
