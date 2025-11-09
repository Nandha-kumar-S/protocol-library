import React from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import styled from 'styled-components'
import { FiUpload, FiClock, FiCheckCircle, FiSearch, FiChevronLeft, FiChevronRight, FiGrid, FiTable } from 'react-icons/fi'

const SidebarContainer = styled.aside`
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: ${props => props.collapsed ? '60px' : '280px'};
  background: #f8f9fa;
  border-right: 1px solid #dee2e6;
  transition: width 0.3s ease;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
  
  @media (max-width: 768px) {
    transform: translateX(${props => props.collapsed ? '-100%' : '0'});
    width: 280px;
  }
`

const HeaderSection = styled.div`
  padding: ${props => props.collapsed ? '15px 10px' : '20px'};
  border-bottom: 1px solid #dee2e6;
  display: flex;
  align-items: center;
  justify-content: ${props => props.collapsed ? 'center' : 'flex-start'};
  gap: 12px;
  background: #f8f9fa;
  min-height: 80px;
  
  img {
    width: ${props => props.collapsed ? '30px' : '40px'};
    height: ${props => props.collapsed ? '30px' : '40px'};
    object-fit: contain;
    flex-shrink: 0;
  }
  
  .title-text {
    display: ${props => props.collapsed ? 'none' : 'block'};
    color: #2c3e50;
    font-size: 1.4rem;
    font-weight: 600;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
  }
`

const Navigation = styled.nav`
  flex: 1;
  padding: ${props => props.collapsed ? '10px' : '20px'};
  overflow: hidden;
`

const NavItem = styled.div`
  display: flex;
  align-items: center;
  padding: ${props => props.collapsed ? '12px 0' : '16px 20px'};
  color: #2c3e50;
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
  margin-bottom: 8px;
  border-radius: 12px;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 500;
  justify-content: ${props => props.collapsed ? 'center' : 'flex-start'};
  
  &:hover {
    background: #e9ecef;
    transform: ${props => props.collapsed ? 'none' : 'translateX(5px)'};
  }
  
  &.active {
    background: #007bff;
    color: white;
  }
  
  svg {
    width: 22px;
    height: 22px;
    margin-right: ${props => props.collapsed ? '0' : '16px'};
    flex-shrink: 0;
  }
  
  span {
    display: ${props => props.collapsed ? 'none' : 'block'};
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
`

const ToggleButton = styled.button`
  position: absolute;
  right: -15px;
  top: 20px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: white;
  border: 2px solid #dee2e6;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  
  &:hover {
    transform: scale(1.1);
    background: #f8f9fa;
  }
  
  svg {
    width: 16px;
    height: 16px;
    color: #2c3e50;
  }
`

const menuItems = [
  { path: '/upload', icon: FiTable, label: 'Document Manager' },
  { path: '/jobs', icon: FiGrid, label: 'All Jobs' },
  // { path: '/jobs/in-progress', icon: FiClock, label: 'In Progress Jobs' }
]

const Sidebar = ({ collapsed, onToggle }) => {
  const navigate = useNavigate()
  const location = useLocation()
  
  const isActive = (path) => {
    return location.pathname === path || 
           (path === '/upload' && location.pathname === '/')
  }
  
  return (
    <SidebarContainer collapsed={collapsed}>
      <HeaderSection collapsed={collapsed}>
        <img 
          src="/app-logo.svg" 
          alt="App Logo"
        />
        <h2 className="title-text">Protocol Library</h2>
      </HeaderSection>
      
      <Navigation>
        {menuItems.map((item) => (
          <NavItem
            key={item.path}
            collapsed={collapsed}
            className={isActive(item.path) ? 'active' : ''}
            onClick={() => navigate(item.path)}
          >
            <item.icon />
            <span>{item.label}</span>
          </NavItem>
        ))}
      </Navigation>
      
      <ToggleButton onClick={onToggle}>
        {collapsed ? <FiChevronRight /> : <FiChevronLeft />}
      </ToggleButton>
    </SidebarContainer>
  )
}

export default Sidebar;
