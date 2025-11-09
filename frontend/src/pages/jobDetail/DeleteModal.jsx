import React from 'react';
import { Modal, ModalContent } from './styles';
import { FiAlertTriangle } from 'react-icons/fi';

const DeleteModal = ({ section, onConfirm, onClose }) => {
  return (
    <Modal onClick={onClose}>
      <ModalContent onClick={e => e.stopPropagation()} style={{ maxWidth: 400, textAlign: 'center', padding: '2rem 2rem 1.5rem' }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginBottom: 16 }}>
          <FiAlertTriangle size={48} color="#dc3545" style={{ marginBottom: 8 }} />
          <h2 style={{ color: '#dc3545', margin: 0 }}>Delete Section</h2>
        </div>
        <p style={{ fontSize: '1rem', color: '#4b5563', marginBottom: 8 }}>
          Are you sure you want to delete this section?
        </p>
  
        <div style={{ marginTop: '32px', display: 'flex', gap: '16px', justifyContent: 'center' }}>
          <button 
            onClick={onClose}
            style={{
              padding: '10px 24px',
              background: '#f8f9fa',
              border: '1px solid #dee2e6',
              borderRadius: '6px',
              fontWeight: 500,
              fontSize: '1rem',
              cursor: 'pointer',
              minWidth: 100
            }}
          >
            Cancel
          </button>
          <button 
            onClick={onConfirm}
            style={{
              padding: '10px 24px',
              background: '#dc3545',
              color: 'white',
              border: 'none',
              borderRadius: '6px',
              fontWeight: 500,
              fontSize: '1rem',
              cursor: 'pointer',
              minWidth: 100
            }}
          >
            Delete
          </button>
        </div>
      </ModalContent>
    </Modal>
  );
};

export default DeleteModal;
