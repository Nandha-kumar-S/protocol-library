import React from 'react';
import styled from 'styled-components';
import { 
  FiClock, 
  FiAlertCircle, 
  FiCheckCircle, 
  FiActivity,
  FiFileText,
  FiLayers,
  FiLink,
  FiMap,
  FiPause
} from 'react-icons/fi';
import { STATUS_MAPPING, STATUS_STAGES } from '../../utils/statusUtils';

const StatusContainer = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  background: ${props => props.background};
  color: ${props => props.color};
`;

// Utility to get contrast color (black or white) for a given background
const getContrastColor = (bgColor) => {
  // Remove hash if present
  const color = bgColor.charAt(0) === '#' ? bgColor.substring(1, 7) : bgColor;
  // Convert to RGB
  const r = parseInt(color.substring(0,2), 16);
  const g = parseInt(color.substring(2,4), 16);
  const b = parseInt(color.substring(4,6), 16);
  // Calculate luminance
  const luminance = (0.299*r + 0.587*g + 0.114*b)/255;
  return luminance > 0.6 ? '#222' : '#fff';
};

const getStatusConfig = (status) => {
  // Map backend status to display status
  const displayStatus = STATUS_MAPPING[status] || status;
  // Find color from STATUS_STAGES
  const stage = STATUS_STAGES.find(s => s.key === displayStatus);
  const background = stage ? stage.color : '#6c757d';
  const contrastColor = getContrastColor(background);
  const configs = {
    Started: {
      icon: FiClock,
      background,
      color: contrastColor
    },
    'Document Analysis': {
      icon: FiFileText,
      background,
      color: contrastColor
    },
    'Extracting Protocol Details': {
      icon: FiLayers,
      background,
      color: contrastColor
    },
    'Standardising to schemas': {
      icon: FiMap,
      background,
      color: contrastColor
    },
    'Generating Network': {
      icon: FiLink,
      background,
      color: contrastColor
    },
    Completed: {
      icon: FiCheckCircle,
      background,
      color: contrastColor
    },
    Failed: {
      icon: FiAlertCircle,
      background,
      color: contrastColor
    }
  };
  return configs[displayStatus] || configs.Started;
};

const StatusBadge = ({ status }) => {
  const config = getStatusConfig(status);
  const Icon = config.icon;

  // Show mapped display status
  const displayStatus = STATUS_MAPPING[status] || status;
  return (
    <StatusContainer background={config.background} color={config.color}>
      <Icon />
      {displayStatus}
    </StatusContainer>
  );
};

export default StatusBadge;
