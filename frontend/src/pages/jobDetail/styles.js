import styled from 'styled-components';

export const PageContainer = styled.div`
  padding: 20px 40px;
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 20px;
`;

export const Header = styled.div`
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 30px;
`;

export const PageTitle = styled.h1`
  font-size: 24px;
  font-weight: 600;
  color: #2d3748;
  margin: 0;
`;

export const BackIconButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  color: #495057;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
  
  &:hover {
    background: #e9ecef;
  }
  
  svg {
    flex-shrink: 0;
  }
`;

export const JobDetailCard = styled.div`
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  width: 100%;
`;

export const JobInfo = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
`;

export const JobTitle = styled.h2`
  font-size: 20px;
  font-weight: 600;
  color: #334155;
  margin: 0 0 8px 0;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
`;

export const JobMeta = styled.div`
  display: flex;
  gap: 24px;
  color: #64748b;
  font-size: 14px;
  flex-wrap: wrap;
  row-gap: 8px;
`;

export const MetaItem = styled.div`
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.875rem;
  color: #64748b;
  
  svg {
    color: #94a3b8;
    flex-shrink: 0;
  }
  
  strong {
    color: #334155;
    font-weight: 500;
    margin-left: 2px;
  }
`;

export const StatusBadge = styled.div`
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  
  &.in-progress {
    background-color: #FEF3C7;
    color: #92400E;
  }
  
  &.completed {
    background-color: #DEF7EC;
    color: #03543F;
  }
  
  &.failed {
    background-color: #FEE2E2;
    color: #991B1B;
  }
`;

export const Modal = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
`;

export const ModalContent = styled.div`
  background: white;
  padding: 24px;
  border-radius: 12px;
  max-width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
`;

export const TableContainer = styled.div`
  margin-top: 12px;
  overflow-x: auto;
  max-width: 100%;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  background: white;
`;

export const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  min-width: 600px;
  
  th, td {
    border: 1px solid #e2e8f0;
    padding: 8px 12px;
    text-align: left;
    font-size: 0.85rem;
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  th {
    background: #f8fafc;
    font-weight: 600;
    color: #475569;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.5px;
    padding: 10px 12px;
  }
  
  tr:hover {
    background-color: #f8fafc;
  }
  
  td {
    color: #334155;
  }
`;

export const JobContent = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
`;

export const SectionContainer = styled.div`
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;
  width: 100%;
  
  &:hover {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
`;

export const SectionContent = styled.div`
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
`;

export const SectionDiv = styled.div`
    display: flex;
    flex-direction: column;
    padding: 16px;
`;

export const ActionButton = styled.button`
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    color: white;
    
    &:hover {
        opacity: 0.9;
    }
`;
