import React, { useState } from 'react';
import { FiTrash2, FiEye, FiChevronLeft, FiChevronRight } from 'react-icons/fi';
import styled from 'styled-components';
import { useToast } from '../../contexts/ToastContext';

// Styled Components
const JobContent = styled.div`
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
`;

const SectionContainer = styled.div`
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;
  width: 100%;
  
  &:hover {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
`;

const SectionTitle = styled.h3`
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid #e5e7eb;
  text-transform: capitalize;
`;

const SectionContent = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
`;

const ItemCard = styled.div`
      display: flex;
    justify-content: space-between;
    align-items: start;
  background: ${props => props.isEven ? '#f9fafb' : 'white'};
  border-radius: 8px;
  padding: 1.25rem;
  transition: all 0.2s ease;
  border: 1px solid #e5e7eb;
  
  &:hover {
    border-color: #d1d5db;
  }
`;

const ItemHeader = styled.h4`
  font-size: 1rem;
  font-weight: 500;
  color: #111827;
  margin-bottom: 0.75rem;
`;

const ItemContent = styled.p`
  font-size: 0.9375rem;
  color: #4b5563;
  line-height: 1.6;
  margin-bottom: 1rem;
  white-space: pre-wrap;
`;

const ActionButtons = styled.div`
  display: flex;
  gap: 0.75rem;
`;

const Button = styled.button`
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  
  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
  
  &:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
`;

const ViewButton = styled(Button)`
  min-width: 100px;
  height: 32px;
  background-color: #3b82f6;
  color: white;
  justify-content: center;
  white-space: nowrap;
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
  
  &:hover:not(:disabled) {
    background-color: #2563eb;
  }
`;

const DeleteButton = styled(Button)`
  min-width: 100px;
  height: 32px;
  background-color: #fef2f2;
  color: #dc2626;
  border-color: #fecaca;
  justify-content: center;
  white-space: nowrap;
  padding: 0.4rem 0.75rem;
  font-size: 0.8rem;
  
  &:hover:not(:disabled) {
    background-color: #fee2e2;
  }
`;

const ModalOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
`;

const ModalContent = styled.div`
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  overflow: auto;
  padding: 1.5rem;
  position: relative;
`;

const CloseButton = styled.button`
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #6b7280;
  
  &:hover {
    color: #374151;
  }
`;

const TableContainer = styled.div`
  margin-top: 1rem;
  overflow-x: auto;
  
  table {
    width: 100%;
    border-collapse: collapse;
    
    th, td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid #e5e7eb;
    }
    
    th {
      background-color: #f9fafb;
      font-weight: 600;
      color: #374151;
    }
    
    tr:hover {
      background-color: #f9fafb;
    }
  }
`;

const SectionView = ({ sections = {}, onViewTable, onDelete, currentSection, jobStatus }) => {
  // Convert sections object to array for easier mapping
  const [currentSchemaIndex, setCurrentSchemaIndex] = useState(0);
  const { showError } = useToast();
  
  const schemaKeys = Object.keys(sections);
  const currentSchemaKey = schemaKeys[currentSchemaIndex];
  const currentSchema = sections[currentSchemaKey];
  
  const navigateSchema = (direction) => {
    if (direction === 'prev' && currentSchemaIndex > 0) {
      setCurrentSchemaIndex(prev => prev - 1);
    } else if (direction === 'next' && currentSchemaIndex < schemaKeys.length - 1) {
      setCurrentSchemaIndex(prev => prev + 1);
    }
  };

  const handleViewTable = (item) => {
    try {
      if (item) {
        onViewTable(item);
      }
    } catch (error) {
      showError('Failed to open table view');
    }
  };

  const handleDelete = (item) => {
    onDelete(item);
  };

  const renderItem = (item, index) => (
    <ItemCard key={index} isEven={index % 2 === 0}>
      <div>
        {item.title && <ItemHeader>{item.title}</ItemHeader>}
        {item.extracted_text && <ItemContent>{item.extracted_text}</ItemContent>}
      </div>
      <ActionButtons>
        {item.extracted_tables?.length > 0 && (
          <ViewButton onClick={() => handleViewTable(item)}>
            <FiEye size={14} /> View Table
          </ViewButton>
        )}
        {jobStatus === 'CONTENT_EXTRACTION_PAUSED' && (
          <DeleteButton 
            onClick={() => handleDelete(item)}
          >
            <FiTrash2 size={14} /> Delete
          </DeleteButton>
        )}
      </ActionButtons>
    </ItemCard>
  );

  return (
    <JobContent>
      <SectionContainer>
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center',
          marginBottom: '1rem'
        }}>
          <button
            onClick={() => navigateSchema('prev')}
            disabled={currentSchemaIndex === 0}
            style={{
              background: 'none',
              border: 'none',
              cursor: 'pointer',
              color: currentSchemaIndex === 0 ? '#d1d5db' : '#4b5563',
              padding: '0.5rem',
              borderRadius: '4px',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              opacity: currentSchemaIndex === 0 ? 0.5 : 1,
              pointerEvents: currentSchemaIndex === 0 ? 'none' : 'auto'
            }}
          >
            <FiChevronLeft size={20} />
            Previous
          </button>
          
          <SectionTitle style={{ margin: 0, textAlign: 'center' }}>
            {currentSchemaKey ? currentSchemaKey.replace(/([A-Z])/g, ' $1').trim() : ''}
            <div style={{ fontSize: '0.875rem', color: '#6b7280', marginTop: '0.25rem' }}>
              {currentSchemaIndex + 1} of {schemaKeys.length}
            </div>
          </SectionTitle>
          
          <button
            onClick={() => navigateSchema('next')}
            disabled={currentSchemaIndex === schemaKeys.length - 1}
            style={{
              background: 'none',
              border: 'none',
              cursor: 'pointer',
              color: currentSchemaIndex === schemaKeys.length - 1 ? '#d1d5db' : '#4b5563',
              padding: '0.5rem',
              borderRadius: '4px',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              opacity: currentSchemaIndex === schemaKeys.length - 1 ? 0.5 : 1,
              pointerEvents: currentSchemaIndex === schemaKeys.length - 1 ? 'none' : 'auto'
            }}
          >
            Next
            <FiChevronRight size={20} />
          </button>
        </div>
        
        <SectionContent>
          {currentSchema?.items?.length > 0 ? (
            currentSchema.items.map((item, index) => renderItem(item, index))
          ) : (
            <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
              No items found in this schema
            </div>
          )}
        </SectionContent>
      </SectionContainer>
    </JobContent>
  );
};

export default SectionView;
