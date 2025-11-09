import React, { useState } from 'react'
import { useLocation } from 'react-router-dom'
import styled from 'styled-components'
import Header from './Header'
import Sidebar from './Sidebar'
import FullscreenProvider from '../FullscreenProvider/FullscreenProvider'

const LayoutContainer = styled.div`
  display: flex;
  min-height: 100vh;
  background-color: #f8f9fa;
`

const MainContent = styled.main`
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-left: ${props => props.sidebarCollapsed ? '60px' : '280px'};
  transition: margin-left 0.3s ease;
  
  @media (max-width: 768px) {
    margin-left: 0;
  }
`

const ContentArea = styled.div`
  flex: 1;
  padding: 20px;
  overflow-y: auto;
`

const Layout = ({ children }) => {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const location = useLocation()

  // Auto-collapse sidebar when route includes 'viewer/'
  React.useEffect(() => {
    if (location.pathname.includes('viewer/')) {
      setSidebarCollapsed(true)
    } else {
      setSidebarCollapsed(false)
    }
  }, [location.pathname])

  const toggleSidebar = () => {
    setSidebarCollapsed(!sidebarCollapsed)
  }

  return (
    <FullscreenProvider>
      <LayoutContainer>
        <Sidebar collapsed={sidebarCollapsed} onToggle={toggleSidebar} />
        <MainContent sidebarCollapsed={sidebarCollapsed}>
          <Header currentPath={location.pathname} />
          <ContentArea>
            {children}
          </ContentArea>
        </MainContent>
      </LayoutContainer>
    </FullscreenProvider>
  )
}

export default Layout
