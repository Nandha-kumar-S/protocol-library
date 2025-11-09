import React, { useState } from 'react';
import { FiX, FiChevronDown, FiChevronUp } from 'react-icons/fi';
import { Modal, ModalContent, TableContainer, Table } from './styles';
import styled from 'styled-components';

// Styled Components
const Accordion = styled.div`
  width: 100%;
  margin-bottom: 8px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  background: white;
`;

const AccordionHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background-color: #f8fafc;
  cursor: pointer;
  transition: background-color 0.2s ease;
  border-bottom: 1px solid #e2e8f0;
  
  &:hover {
    background-color: #f1f5f9;
  }
  
  h3 {
    margin: 0;
    font-size: 0.95rem;
    font-weight: 500;
    color: #1e293b;
  }
`;

const AccordionContent = styled.div`
  max-height: ${props => (props.isOpen ? '1000px' : '0')};
  overflow: hidden;
  transition: max-height 0.3s ease-in-out;
`;

const TableWrapper = styled.div`
  padding: 16px;
  background: white;
`;

const EmptyState = styled.div`
  text-align: center;
  padding: 20px;
  color: #64748b;
  font-style: italic;
`;

const TableModal = ({ section, onClose }) => {
  const [openIndex, setOpenIndex] = useState(0);
  const tables = section?.extracted_tables || [];

  const toggleAccordion = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <Modal onClick={onClose}>
      <ModalContent onClick={e => e.stopPropagation()}>
        <div style={{ 
          display: 'flex', 
          justifyContent: 'space-between', 
          alignItems: 'center', 
          marginBottom: '20px',
          paddingBottom: '16px',
          borderBottom: '1px solid #e2e8f0'
        }}>
          <h2 style={{ margin: 0, fontSize: '1.25rem', color: '#1e293b' }}>{section?.title || 'Table View'}</h2>
          <button 
            onClick={onClose} 
            style={{ 
              background: 'none', 
              border: 'none', 
              cursor: 'pointer',
              color: '#64748b',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: '32px',
              height: '32px',
              borderRadius: '6px',
              transition: 'background-color 0.2s',
              '&:hover': {
                backgroundColor: '#f1f5f9'
              }
            }}
          >
            <FiX size={20} />
          </button>
        </div>
        
        <TableContainer>
          {tables.length === 0 ? (
            <EmptyState>No tables available</EmptyState>
          ) : (
            tables.map((table, index) => (
              <Accordion key={index}>
                <AccordionHeader 
                  onClick={() => toggleAccordion(index)}
                  aria-expanded={openIndex === index}
                  aria-controls={`table-${index}`}
                >
                  <h3>Table {index + 1}{table.title ? `: ${table.title}` : ''}</h3>
                  {openIndex === index ? <FiChevronUp /> : <FiChevronDown />}
                </AccordionHeader>
                <AccordionContent 
                  id={`table-${index}`}
                  isOpen={openIndex === index}
                >
                  <TableWrapper>
                    <Table>
                      <thead>
                        <tr>
                          {table.columns?.map((header, i) => (
                            <th key={i}>{header || `Column ${i + 1}`}</th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {table.data?.length > 0 ? (
                          table.data.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                              {row.map((cell, cellIndex) => (
                                <td key={cellIndex}>{cell || '-'}</td>
                              ))}
                            </tr>
                          ))
                        ) : (
                          <tr>
                            <td colSpan={table.columns?.length || 1} style={{ textAlign: 'center', color: '#64748b' }}>
                              No data available
                            </td>
                          </tr>
                        )}
                      </tbody>
                    </Table>
                  </TableWrapper>
                </AccordionContent>
              </Accordion>
            ))
          )}
        </TableContainer>
      </ModalContent>
    </Modal>
  );
};

export default TableModal;
