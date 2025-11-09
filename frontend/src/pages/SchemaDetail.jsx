import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import styled from 'styled-components'
import { FiArrowLeft, FiMaximize2, FiMinimize2, FiChevronLeft, FiChevronRight } from 'react-icons/fi'
import Editor from '@monaco-editor/react'
import { getJob } from '../services/jobService'
import { jobAPI } from '../services/api'

const PageContainer = styled.div`
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f8f9fa;
`

const Header = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  background: white;
  border-bottom: 1px solid #dee2e6;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`

const HeaderLeft = styled.div`
  display: flex;
  align-items: center;
  gap: 16px;
`

const BackButton = styled.button`
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  color: #007bff;
  cursor: pointer;
  font-size: 0.9rem;
  padding: 8px 12px;
  border-radius: 6px;
  transition: background 0.2s ease;
  
  &:hover {
    background: #f8f9fa;
  }
`

const HeaderTitle = styled.div`
  display: flex;
  flex-direction: column;
  gap: 4px;
`

const Breadcrumb = styled.div`
  font-size: 0.875rem;
  color: #6c757d;
  margin-bottom: 1rem;
`

const SectionCounter = styled.span`
  font-size: 0.9rem;
  color: #495057;
  white-space: nowrap;
  min-width: 80px;
  text-align: center;
  font-weight: 500;
`

const SchemaTitle = styled.h1`
  margin: 0;
  font-size: 1.2rem;
  color: #2c3e50;
  font-weight: 600;
`

const FullscreenButton = styled.button`
  display: flex;
  align-items: center;
  gap: 8px;
  background: #007bff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s ease;
  
  &:hover {
    background: #0056b3;
  }
`

const ContentContainer = styled.div`
  flex: 1;
  display: flex;
  gap: 16px;
  padding: 16px;
  overflow: hidden;
  width: 100%;
`

const ContentPanel = styled.div`
  flex: 1;
  background: white;
  border-radius: 8px;
  border: 1px solid #dee2e6;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  width: 50%;
`

const PanelHeader = styled.div`
  padding: 16px 20px;
  background: #f8f9fa;
  border-bottom: 1px solid #dee2e6;
  font-weight: 600;
  color: #2c3e50;
  display: flex;
  justify-content: space-between;
  align-items: center;
`

const PanelContent = styled.div`
  flex: 1;
  overflow: auto;
  padding: 20px;
`

const JsonPanelContent = styled.div`
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
`

const SectionItem = styled.div`
  padding: 12px 16px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  margin-bottom: 12px;
  background: #f8f9fa;
`

const SectionTitle = styled.div`
  font-weight: 600;
  color: #dc3545;
  margin-bottom: 8px;
`

const SectionText = styled.div`
  color: #495057;
  line-height: 1.5;
`

const ViewToggle = styled.div`
  display: flex;
  gap: 8px;
`

const ToggleButton = styled.button`
  padding: 6px 12px;
  border: 1px solid #dee2e6;
  background: ${props => props.active ? '#007bff' : 'white'};
  color: ${props => props.active ? 'white' : '#495057'};
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.2s ease;
  
  &:hover {
    background: ${props => props.active ? '#0056b3' : '#f8f9fa'};
  }
`

const FullscreenOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: white;
  z-index: 2000;
  display: flex;
  flex-direction: column;
`

const NavigationControls = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
`

const NavButton = styled.button`
  padding: 4px 8px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s ease;
  
  &:hover {
    background: #f8f9fa;
  }
`

const SchemaDetail = () => {
  const { id } = useParams()
  const navigate = useNavigate()
  const [schema, setSchema] = useState(null)
  const [isFullscreen, setIsFullscreen] = useState(false)
  const [jsonView, setJsonView] = useState('nested')
  const [sections, setSections] = useState([])
  const [currentSection, setCurrentSection] = useState(0)

  useEffect(() => {
    let isMounted = true;

    const fetchAndProcessJobData = async () => {
      try {
        const response = await getJob(id);
        const transformedJob = {
          id: id,
          protocolId: 'PROT-' + id,
          title: response.json_type || 'Protocol Document',
          status: 'Completed',
          sections: Object.entries(response.json_value || {}).reduce((acc, [key, value]) => {
            if (Array.isArray(value) && value.length > 0) {
              // Only process arrays that have items with meaningful content
              const processedItems = value
                .map(item => {
                  try {
                    return {
                      title: item.title || '',
                      extracted_text: item.extracted_text || '',
                      extracted_tables: (item.extracted_tables || []).map(table => ({
                        columns: table.columns,
                        data: Array.isArray(table.data) ? table.data : []
                      }))
                    };
                  } catch (error) {
                    console.error('Error processing item in section', key, error);
                    return null;
                  }
                })
                .filter(item =>
                  item && (
                    item.title ||
                    item.extracted_text ||
                    (item.extracted_tables && item.extracted_tables.length > 0)
                  )
                );

              // Only add sections that have valid items
              if (processedItems.length > 0) {
                acc[key] = {
                  id: key,
                  title: key,
                  items: processedItems
                };
              }
            }
            return acc;
          }, {})
        };
        setSchema(transformedJob);

      } catch (error) {
        console.error('Error fetching job data:', error);
        if (isMounted) {
          // Set schema with error state
          setSchema({
            id: id,
            name: 'Error',
            protocolId: 'N/A',
            confidence: '0%',
            error: 'Failed to load job data'
          });
        }
      }
    };

    fetchAndProcessJobData();

    return () => {
      isMounted = false;
    };
  }, [id])

  const toggleFullscreen = () => {
    setIsFullscreen(!isFullscreen)
  }

  const handleNextSection = () => {
    if (currentSection < sections.length - 1) {
      const nextSection = currentSection + 1;
      setCurrentSection(nextSection);
      setSchema(prev => ({
        ...prev,
        currentSection: sections[nextSection],
        data: Array.isArray(sections[nextSection]) ? sections[nextSection] : []
      }));
    }
  };

  const handlePrevSection = () => {
    if (currentSection > 0) {
      const prevSection = currentSection - 1;
      setCurrentSection(prevSection);
      setSchema(prev => ({
        ...prev,
        currentSection: sections[prevSection],
        data: Array.isArray(sections[prevSection]) ? sections[prevSection] : []
      }));
    }
  };

  if (!schema) {
    return (
      <PageContainer>
        <div style={{ padding: '20px' }}>Loading schema details...</div>
      </PageContainer>
    )
  }

  // Styled components for better organization
  const SectionHeader = styled.div`
  background: #f8f9fa;
  padding: 12px 16px;
  border-radius: 6px;
  margin-bottom: 16px;
  border-left: 4px solid #007bff;
`;

  const SectionTitle = styled.h2`
  font-size: 1.25rem;
  margin: 0 0 8px 0;
  color: #2c3e50;
`;

  const SectionSubtitle = styled.div`
  font-size: 0.9rem;
  color: #6c757d;
  margin-bottom: 4px;
`;

  const StyledTable = styled.table`
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin: 16px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-radius: 6px;
  overflow: hidden;

  th {
    background-color: #f1f5f9;
    color: #334155;
    font-weight: 600;
    text-align: left;
    padding: 12px 16px;
    border-bottom: 2px solid #e2e8f0;
  }

  td {
    padding: 12px 16px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr:hover {
    background-color: #f8fafc;
  }
`;

  const ContentWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
`;

  const SectionNavigation = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: white;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 16px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
`;

  const NavButton = styled.button`
  display: flex;
  align-items: center;
  gap: 8px;
  background: ${props => props.disabled ? '#f1f5f9' : '#f8fafc'};
  border: 1px solid #e2e8f0;
  color: ${props => props.disabled ? '#94a3b8' : '#334155'};
  padding: 8px 16px;
  border-radius: 6px;
  cursor: ${props => props.disabled ? 'not-allowed' : 'pointer'};
  transition: all 0.2s ease;
  font-weight: 500;
  
  &:not(:disabled):hover {
    background: #f1f5f9;
    border-color: #cbd5e1;
  }
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
  overflow:auto;
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
`;

  const ContentComponent = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [currentSchemaIndex, setCurrentSchemaIndex] = useState(0);
    console.debug("schema?.sections", schema?.sections)
    const schemaKeys = Object.keys(schema?.sections);
    const currentSchemaKey = schemaKeys[currentSchemaIndex];
    const currentSchema = schema?.sections[currentSchemaKey];
    const [currentJson, setCurrentJson] = useState();

    console.debug("schemaKeys", currentSchema)

    const navigateSchema = (direction) => {
      if (direction === 'prev' && currentSchemaIndex > 0) {
        setCurrentSchemaIndex(prev => prev - 1);
      } else if (direction === 'next' && currentSchemaIndex < schemaKeys.length - 1) {
        setCurrentSchemaIndex(prev => prev + 1);
      }
    };
    const renderItem = (item, index) => (
      <ItemCard key={index} isEven={index % 2 === 0}>
        <div>
          {item.title && <ItemHeader>{item.title}</ItemHeader>}
          {item.extracted_text && <ItemContent>{item.extracted_text}</ItemContent>}
        </div>
      </ItemCard>
    );

    // Fetch schema data when currentSchemaIndex changes
    useEffect(() => {
      const fetchSchemaData = async () => {
        if (!schema?.id || !currentSchemaKey) return;

        setIsLoading(true);
        try {

          const { data } = await jobAPI.getSchema(schema.id, currentSchemaKey);

          console.log("response", data)
          setCurrentJson(data);
        } catch (error) {
          console.error('Error fetching schema data:', error);
          // Fallback to the original data if API call fails
          setCurrentJson(schema?.sections?.[currentSchemaKey]);
        } finally {
          setIsLoading(false);
        }
      };

      fetchSchemaData();
    }, [currentSchemaIndex, schema?.id, currentSchemaKey]);

    return (
      <>
        <Header>
          <HeaderLeft>
            <BackButton onClick={() => navigate(-1)}>
              <FiArrowLeft />
              Back to Jobs
            </BackButton>
            <HeaderTitle>
              <Breadcrumb>
                Protocol Library &gt; {schema.id} &gt; Schema Details
              </Breadcrumb>
              <SchemaTitle>
                {schema.id} - {schema?.title || 'Document Sections'}
              </SchemaTitle>
            </HeaderTitle>
          </HeaderLeft>
          <FullscreenButton onClick={toggleFullscreen}>
            {isFullscreen ? <FiMinimize2 /> : <FiMaximize2 />}
            {isFullscreen ? 'Exit Fullscreen' : 'Fullscreen'}
          </FullscreenButton>
        </Header>

        <SectionNavigation>
          <div>
            <SectionSubtitle>Current Section</SectionSubtitle>
            <SectionTitle>{currentSchemaKey.replace(/([A-Z])/g, ' $1').trim()}</SectionTitle>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <NavButton
              onClick={() => navigateSchema('prev')}
              disabled={currentSchemaIndex === 0}
            >
              <FiChevronLeft size={18} />
              Previous
            </NavButton>
            <div style={{ fontSize: '0.875rem', color: '#6b7280', marginTop: '0.25rem' }}>
              {currentSchemaIndex + 1} of {schemaKeys.length}
            </div>
            <NavButton
              onClick={() => navigateSchema('next')}
              disabled={currentSchemaIndex === schema?.sections?.length - 1}
            >
              Next
              <FiChevronRight size={18} style={{ marginLeft: '8px' }} />
            </NavButton>
          </div>
        </SectionNavigation>

        <ContentContainer>
          <ContentPanel>
            <PanelHeader>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span>Document Content</span>
              </div>
            </PanelHeader>
            <PanelContent>
              <ContentWrapper>
                {currentSchema?.items?.length > 0 ? (
                  currentSchema.items.map((item, index) => renderItem(item, index))
                ) : (
                  <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>
                    No items found in this schema
                  </div>
                )}
              </ContentWrapper>
            </PanelContent>
          </ContentPanel>

          <ContentPanel>
            <PanelHeader>
              Extracted Data (removable id level)
              <ViewToggle>
                <ToggleButton
                  active={jsonView === 'nested'}
                  onClick={() => setJsonView('nested')}
                >
                  Nested JSON data view
                </ToggleButton>
                <ToggleButton
                  active={jsonView === 'editor'}
                  onClick={() => setJsonView('editor')}
                >
                  JSON Editor
                </ToggleButton>
              </ViewToggle>
            </PanelHeader>
            <JsonPanelContent>
              {jsonView === 'nested' ? (
                <PanelContent>
                  <pre style={{
                    background: '#f8f9fa',
                    padding: '16px',
                    borderRadius: '6px',
                    fontSize: '0.9rem',
                    lineHeight: '1.4',
                    margin: 0,
                    overflowX: 'auto',
                    whiteSpace: 'pre-wrap',
                    wordWrap: 'break-word',
                  }}>
                    {JSON.stringify(currentJson, null, 2)}
                  </pre>
                </PanelContent>
              ) : (
                <div style={{ flex: 1, minHeight: 0 }}>
                  <Editor
                    height="100%"
                    defaultLanguage="json"
                    value={JSON.stringify(currentJson, null, 2)}
                    theme="vs-light"
                    options={{
                      minimap: { enabled: false },
                      scrollBeyondLastLine: false,
                      fontSize: 14,
                      lineNumbers: 'on',
                      roundedSelection: false,
                      scrollbar: {
                        vertical: 'visible',
                        horizontal: 'visible'
                      }
                    }}
                  />
                </div>
              )}
            </JsonPanelContent>
          </ContentPanel>
        </ContentContainer>
      </>
    )
  }

  return isFullscreen ? (
    <FullscreenOverlay>
      <ContentComponent />
    </FullscreenOverlay>
  ) : (
    <PageContainer>
      <ContentComponent />
    </PageContainer>
  )
}

export default SchemaDetail
