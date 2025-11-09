import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import { FiDownload, FiFileText } from 'react-icons/fi';
import { saveAs } from 'file-saver';
import DownloadButton from '../../components/DownloadButton/DownloadButton';
import { useToast } from '../../contexts/ToastContext';
import { jobsApi } from '../../services/jobsApi';
import axios from 'axios';

// Commented out components that need to be recreated
import JsonTreeView from './JsonTreeView';
import DiagramCanvas from './DiagramCanvas';

// Component
const USDMViewer = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(true);
  const [diagramData, setDiagramData] = useState(null);
  const [fullJsonData, setFullJsonData] = useState(null);
  const [displayName, setDisplayName] = useState('');
  const [isMaximized, setIsMaximized] = useState(false);
  const { showSuccess, showError } = useToast();
  const isInitialMount = useRef(true);
  const diagramRef = useRef(null);


  const handleNodeSelect = (nodeValue, path) => {
    console.log('Selected node:', { nodeValue, path });
    // showSuccess(`Selected: ${path}`);
    setDiagramData(nodeValue);
  };

  const handleUpdateData = (updatedData) => {
    setFullJsonData(updatedData);
    showSuccess('Data updated successfully');
  };

  const handleDownloadExcel = async () => {
    try {
      if (!id) {
        showError('No document ID available for download');
        return;
      }

      const response = await axios(jobsApi.exportToExcel(id));

      // Extract filename from content-disposition header
      const contentDisposition = response.headers['content-disposition'];
      const filenameMatch = contentDisposition && contentDisposition.match(/filename="(.+)"/);
      const filename = filenameMatch ? filenameMatch[1] : `document_${id}_INDIVIDUAL_SCHEMA.xlsx`;

      // Create a blob from the response
      const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
      
      // Trigger download
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
      
      showSuccess('Excel file downloaded successfully');
    } catch (error) {
      console.error('Error downloading Excel file:', error);
      showError(`Failed to download Excel file: ${error.message}`);
    }
  };

  const handleDownload = useCallback(async (format) => {
    if (!diagramRef.current) return;

    try {
      let blob;
      const fileName = `diagram-${new Date().toISOString().split('T')[0]}`;
      
      switch (format) {
        case 'pdf':
          blob = await diagramRef.current.downloadAsPDF();
          saveAs(blob, `${fileName}.pdf`);
          break;
        case 'jpg':
          blob = await diagramRef.current.downloadAsImage('jpeg');
          saveAs(blob, `${fileName}.jpg`);
          break;
        case 'svg':
          blob = await diagramRef.current.downloadAsSVG();
          saveAs(blob, `${fileName}.svg`);
          break;
        default:
          throw new Error('Unsupported format');
      }
      
      showSuccess(`Diagram downloaded as ${format.toUpperCase()}`);
    } catch (error) {
      console.error('Download failed:', error);
      showError(`Failed to download diagram as ${format.toUpperCase()}`);
    }
  }, [showSuccess, showError]);

  const toggleMaximize = () => {
    setIsMaximized(!isMaximized);
  };

  const handleGoBack = () => {
    navigate(-1);
  };

  useEffect(() => {
    if (!isInitialMount.current) {
      // Skip the effect on the initial render in development mode
      return;
    }
    
    isInitialMount.current = false;
    
    const fetchJobData = async () => {
      if (!id) {
        showError('No job ID provided');
        navigate('/jobs');
        return;
      }

      try {
        setIsLoading(true);
        // Fetch job data and schema in parallel
        const schemaResponse = await jobsApi.getJobSchemaById(id);
        const usdmSchema = schemaResponse.data?.json_value;

        if (usdmSchema) {
          // If no job result but we have schema, use the schema as fallback
          setFullJsonData(usdmSchema);
          setDiagramData(usdmSchema);
          setDisplayName('UML Viewer');
          showSuccess('Loaded UML Diagram');
        } else {
          showError('No data available for this job');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        showError('Failed to load job data');
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchJobData();
  }, [id]);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-6">
          <div className="flex items-center gap-4 mb-4">
            <button
              onClick={handleGoBack}
              className="flex items-center gap-2 px-3 py-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors duration-200"
              title="Go back"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              Back
            </button>
            <div className="flex-1">
              <h3 className="text-2xl font-bold text-gray-900">UML Viewer</h3>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={handleDownloadExcel}
                className="flex items-center gap-2 px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                title="Download Excel Report"
              >
                <FiFileText className="w-4 h-4" />
                <span>Export to Excel</span>
              </button>
            </div>
          </div>
        </div>

        {/* Maximized Diagram View */}
        {isMaximized ? (
          <div className="fixed right-5 left-20 top-20 bottom-0 z-50 bg-white">
            <div className="h-full flex flex-col">
              {/* Maximized Header */}
              <div className="flex justify-between items-center p-4 border-b border-gray-200">
                
                <h3 className="font-semibold text-gray-900">UML Diagram</h3>
                <div className="flex items-center gap-2">
                  <DownloadButton onDownload={(format) => handleDownload(format)} />
                  <button
                    onClick={toggleMaximize}
                    className="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200"
                    title="Minimize"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
              </div>
              
              {/* Maximized Diagram Content */}
              <div className="flex-1 p-4">
                {diagramData ? (
                  <DiagramCanvas
                    ref={diagramRef}
                    data={diagramData}
                    fileName={displayName || 'Selected Data'}
                    fullData={fullJsonData}
                    onUpdateData={handleUpdateData}
                  />
                ) : (
                  <div className="flex flex-col items-center justify-center h-full text-gray-500">
                    <svg className="w-16 h-16 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2" />
                    </svg>
                    <h3 className="text-2xl font-medium mb-2">No Diagram Generated</h3>
                    <p className="text-lg">Click on a node in the tree to generate its UML diagram.</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        ) : (
          /* Split View */
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* JSON Tree Viewer */}
            <div className="bg-white rounded-lg shadow-sm border border-gray-200">
              <div className="p-4 border-b border-gray-200 flex justify-between items-center">
                <div>
                  <h2 className="text-lg font-semibold text-gray-900">JSON Structure</h2>
                  {displayName && (
                    <p className="text-sm text-gray-600 mt-1">{displayName}</p>
                  )}
                </div>
                {fullJsonData && (
                  <button
                    onClick={() => {
                      // Get current timestamp in YYYYMMDD-HHMMSS format
                      const now = new Date();
                      const timestamp = now.toISOString()
                        .replace(/[:.]/g, '-')
                        .replace('T', '-')
                        .slice(0, 19);
                      
                      // Get the JSON type from the data structure if available
                      const jsonType = fullJsonData?.type || 'schema';
                      
                      // Create a filename with type and timestamp
                      const filename = `${jsonType}_${timestamp}.json`;
                      
                      const jsonString = JSON.stringify(fullJsonData, null, 2);
                      const blob = new Blob([jsonString], { type: 'application/json' });
                      const url = URL.createObjectURL(blob);
                      const a = document.createElement('a');
                      a.href = url;
                      a.download = filename;
                      document.body.appendChild(a);
                      a.click();
                      document.body.removeChild(a);
                      URL.revokeObjectURL(url);
                    }}
                    className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors duration-200"
                    title="Download JSON"
                  >
                    <FiDownload className="w-5 h-5" />
                  </button>
                )}
              </div>
              <div className="p-4">
                {isLoading ? (
                  <div className="flex items-center justify-center h-96">
                    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
                  </div>
                ) : fullJsonData ? (
                  <div className="h-96 overflow-auto">
                    <JsonTreeView 
                      data={fullJsonData} 
                      onNodeSelect={handleNodeSelect}
                    />
                  </div>
                ) : (
                  <div className="flex flex-col items-center justify-center h-96 text-gray-500">
                    <svg className="w-12 h-12 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <h3 className="text-lg font-medium mb-2">No File Selected</h3>
                    <p className="text-sm">Load sample data or select a JSON file to begin.</p>
                  </div>
                )}
              </div>
            </div>

            {/* Diagram Canvas */}
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 relative">
              <div className="absolute top-2 right-2 z-10 flex gap-2">
                <DownloadButton onDownload={(format) => handleDownload(format)} />
                <button
                  onClick={toggleMaximize}
                  className="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200 bg-white shadow-sm"
                  title="Maximize"
                  disabled={!diagramData}
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
                  </svg>
                </button>
              </div>
              <div className="p-4 border-b border-gray-200">
                <h2 className="text-lg font-semibold text-gray-900">UML Diagram</h2>
              </div>
              <div className="p-4" style={{ height: '500px' }}>
                {diagramData ? (
                  <DiagramCanvas
                    ref={diagramRef}
                    data={diagramData}
                    fileName={displayName || 'Selected Data'}
                    fullData={fullJsonData}
                    onUpdateData={handleUpdateData}
                  />
                ) : (
                  <div className="flex flex-col items-center justify-center h-full text-gray-500">
                    <svg className="w-12 h-12 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2" />
                    </svg>
                    <h3 className="text-lg font-medium mb-2">No Diagram Generated</h3>
                    <p className="text-sm">Click on a node in the tree to generate its UML diagram.</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default USDMViewer;

