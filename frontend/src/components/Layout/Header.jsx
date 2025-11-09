import React from 'react'
import { useNavigate } from 'react-router-dom'
import styled from 'styled-components'
import { FiMenu, FiCommand } from 'react-icons/fi'

const HeaderContainer = styled.header`
  background: white;
  border-bottom: 1px solid #e9ecef;
  padding: 0 20px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 100;
`

const LeftSection = styled.div`
  display: flex;
  align-items: center;
  gap: 15px;
`

const PageTitle = styled.h1`
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
`

const StudyDropdownContainer = styled.div`
  position: relative;
  display: inline-block;
`

const StudyDropdownButton = styled.button`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 200px;
  justify-content: space-between;
  
  &:hover {
    background: #0056b3;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
  }
  
  &:active {
    transform: translateY(0);
  }
  
  .chevron {
    transition: transform 0.2s ease;
    ${props => props.isOpen && 'transform: rotate(180deg);'}
  }
`

const StudyDropdownMenu = styled.div`
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  max-height: 300px;
  overflow-y: auto;
  margin-top: 4px;
  
  ${props => !props.isOpen && 'display: none;'}
`

const StudyDropdownItem = styled.div`
  padding: 12px 16px;
  cursor: pointer;
  border-bottom: 1px solid #f1f3f4;
  transition: all 0.2s ease;
  
  &:last-child {
    border-bottom: none;
  }
  
  &:hover {
    background: #f8f9fa;
  }
  
  &.selected {
    background: #e3f2fd;
    color: #1976d2;
    font-weight: 500;
  }
  
  .study-title {
    font-weight: 500;
    color: #2c3e50;
    margin-bottom: 4px;
  }
  
  .study-meta {
    font-size: 0.8rem;
    color: #6c757d;
  }
`

const EmptyDropdownItem = styled.div`
  padding: 16px;
  text-align: center;
  color: #6c757d;
  font-style: italic;
`

const RightSection = styled.div`
  display: flex;
  align-items: center;
  gap: 15px;
`

const IconButton = styled.button`
  background: none;
  border: none;
  padding: 8px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  
  &:hover {
    background-color: #f8f9fa;
    transform: translateY(-1px);
  }
  
  svg {
    width: 20px;
    height: 20px;
    color: #6c757d;
  }
`

const NotificationBadge = styled.span`
  position: absolute;
  top: -2px;
  right: -2px;
  background: #dc3545;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
`

const NotificationContainer = styled.div`
  position: relative;
`

const getPageTitle = (path) => {
  switch (path) {
    case '/':
      return 'Dashboard'
    case '/protocols':
      return 'Protocols'
    case '/jobs':
      return 'All Jobs'
    case '/upload':
      return 'Document Manager'
    default:
      return 'Protocol Library'
  }
}

const Header = ({ currentPath }) => {
  const navigate = useNavigate()

  const showKeyboardShortcuts = () => {
    // Trigger keyboard shortcuts modal
    const event = new KeyboardEvent('keydown', { key: '?' })
    document.dispatchEvent(event)
  }

  return (
    <HeaderContainer>
      <LeftSection>
        <PageTitle>{getPageTitle(currentPath)}</PageTitle>
      </LeftSection>
      
      <RightSection>
        <IconButton onClick={showKeyboardShortcuts}>
          <FiCommand />
        </IconButton>
      </RightSection>
    </HeaderContainer>
  )
}

export default Header
