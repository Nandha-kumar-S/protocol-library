// components/DiagramCanvas.js
import { useState, useEffect, useMemo, useRef, forwardRef, useImperativeHandle } from 'react';
import * as d3 from 'd3';
import ELK from 'elkjs/lib/elk.bundled.js';
import { useToast } from '../../contexts/ToastContext';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';

const elk = new ELK();

const getValueType = (value) => {
  if (typeof value === 'number') return 'number';
  if (typeof value === 'boolean') return 'boolean';
  return 'string';
};

// Accept new props: fullData and onUpdateData
const DiagramCanvas = forwardRef(({ data, fileName = 'diagram', fullData, onUpdateData }, ref) => {
  const svgRef = useRef();
  const zoomRef = useRef();
  const [zoomLevel, setZoomLevel] = useState(1);
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);
  const [modalOpened, setModalOpened] = useState(false);
  const [activeNode, setActiveNode] = useState(null);
  const [modalMode, setModalMode] = useState('view');
  const [editableFields, setEditableFields] = useState([]);
  const { showSuccess, showError } = useToast();
  
  const [currentData, setCurrentData] = useState(data);

  useEffect(() => {
    setCurrentData(data);
  }, [data]);

  const convertJsonToGraph = useMemo(() => {
    if (!currentData) return { nodes: [], edges: [] };

    const nodes = [];
    const edges = [];
    let nodeIdCounter = 0;

    const processNode = (obj, parentId = null, key = 'root', path = 'root') => {
      const currentNodeId = `node-${nodeIdCounter++}`;
      const keyValuePairs = [];
      let nodeType, nodeTitle;

      if (Array.isArray(obj)) {
        nodeType = 'array';
        nodeTitle = `${key}[]`;
        obj.forEach((item, index) => {
          const itemPath = `${path}[${index}]`;
          if (typeof item === 'object' && item !== null) {
            processNode(item, currentNodeId, `[${index}]`, itemPath);
          } else {
            keyValuePairs.push({ key: `[${index}]`, value: String(item), type: getValueType(item) });
          }
        });
      } else if (typeof obj === 'object' && obj !== null) {
        nodeType = 'object';
        nodeTitle = key;
        Object.entries(obj).forEach(([prop, value]) => {
          const propPath = `${path}.${prop}`;
          if (typeof value === 'object' && value !== null) {
            processNode(value, currentNodeId, prop, propPath);
          } else {
            keyValuePairs.push({ key: prop, value: String(value), type: getValueType(value) });
          }
        });
      } else {
        nodeType = 'primitive';
        nodeTitle = key;
        keyValuePairs.push({ key, value: String(obj), type: getValueType(obj) });
      }

      nodes.push({ id: currentNodeId, text: nodeTitle, keyValuePairs, nodeType, width: 250, height: Math.max(80, 40 + keyValuePairs.length * 22), path });
      if (parentId) {
        edges.push({ id: `edge-${parentId}-${currentNodeId}`, source: parentId, target: currentNodeId });
      }
    };

    processNode(currentData);
    return { nodes, edges };
  }, [currentData]);

  useEffect(() => {
    if (convertJsonToGraph.nodes.length === 0 || !svgRef.current) return;
    const applyLayoutAndRender = async () => {
      const elkNodes = convertJsonToGraph.nodes.map(node => ({
        id: node.id,
        width: node.width,
        height: node.height,
      }));
      const elkEdges = convertJsonToGraph.edges.map(edge => ({
        id: edge.id,
        sources: [edge.source],
        targets: [edge.target],
      }));

      try {
        const graph = await elk.layout({
          id: 'root',
          layoutOptions: {
            'elk.algorithm': 'layered',
            'elk.direction': 'DOWN',
            'elk.spacing.nodeNode': '60',
            'elk.layered.spacing.nodeNodeBetweenLayers': '100',
          },
          children: elkNodes,
          edges: elkEdges,
        });

        const layoutedNodes = convertJsonToGraph.nodes.map(node => {
          const elkNode = graph.children.find(n => n.id === node.id);
          return { ...node, x: elkNode?.x || 0, y: elkNode?.y || 0 };
        });

        setNodes(layoutedNodes);
        setEdges(convertJsonToGraph.edges);
        renderDiagram(layoutedNodes, convertJsonToGraph.edges);
      } catch (error) {
        console.error('ELK layout error:', error);
        showError('Could not apply graph layout.');
      }
    };

    applyLayoutAndRender();
  }, [convertJsonToGraph]);

  const renderDiagram = (localNodes, localEdges) => {
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();
    const width = svg.node().parentElement.clientWidth;
    const height = svg.node().parentElement.clientHeight;
    svg.attr("width", width).attr("height", height);
    const container = svg.append("g");
    const zoom = d3.zoom().scaleExtent([0.2, 4]).on("zoom", (event) => {
      container.attr("transform", event.transform);
      setZoomLevel(event.transform.k);
    });
    zoomRef.current = zoom;
    svg.call(zoom);
    svg.append("defs").append("marker").attr("id", "arrowhead").attr("viewBox", "-0 -5 10 10").attr("refX", 10).attr("refY", 0).attr("orient", "auto").attr("markerWidth", 8).attr("markerHeight", 8).append("path").attr("d", "M0,-5L10,0L0,5").attr("fill", "#555");
    container.selectAll(".edge").data(localEdges).enter().append("line").attr("class", "edge").attr("x1", d => localNodes.find(n => n.id === d.source)?.x + localNodes.find(n => n.id === d.source)?.width / 2).attr("y1", d => localNodes.find(n => n.id === d.source)?.y + localNodes.find(n => n.id === d.source)?.height).attr("x2", d => localNodes.find(n => n.id === d.target)?.x + localNodes.find(n => n.id === d.target)?.width / 2).attr("y2", d => localNodes.find(n => n.id === d.target)?.y).attr("stroke", "#555").attr("stroke-width", 1.5).attr("marker-end", "url(#arrowhead)");
    const nodeGroups = container.selectAll(".node").data(localNodes).enter().append("g").attr("class", "node").attr("transform", d => `translate(${d.x}, ${d.y})`).on("mouseover", function() { d3.select(this).select("rect").attr("stroke-width", 3); }).on("mouseout", function() { d3.select(this).select("rect").attr("stroke-width", 2); });
    nodeGroups.append("rect").attr("width", d => d.width).attr("height", d => d.height).attr("rx", 8).attr("ry", 8).attr("fill", d => ({ array: '#e3f2fd', object: '#f3e5f5', primitive: '#e8f5e8' }[d.nodeType] || '#f5f5f5')).attr("stroke", d => ({ array: '#2196f3', object: '#9c27b0', primitive: '#4caf50' }[d.nodeType] || '#757575')).attr("stroke-width", 2);
    nodeGroups.append("text").attr("x", 10).attr("y", 22).attr("font-size", "14px").attr("font-weight", "bold").text(d => d.text);
    const viewButton = nodeGroups.append("g").style("cursor", "pointer").on("click", (event, d) => { event.stopPropagation(); handleOpenModal(d, 'view'); });
    viewButton.append("circle").attr("cx", d => d.width - 20).attr("cy", 20).attr("r", 12).attr("fill", "#fff").attr("stroke", "#999");
    viewButton.append("text").attr("x", d => d.width - 20).attr("y", 25).attr("text-anchor", "middle").attr("font-size", "14px").attr("fill", "#333").text("👁️");
    // const editButton = nodeGroups.append("g").style("cursor", "pointer").on("click", (event, d) => { event.stopPropagation(); handleOpenModal(d, 'edit'); });
    // editButton.append("circle").attr("cx", d => d.width - 20).attr("cy", 20).attr("r", 12).attr("fill", "#fff").attr("stroke", "#999");
    // editButton.append("text").attr("x", d => d.width - 20).attr("y", 24).attr("text-anchor", "middle").attr("font-size", "12px").attr("fill", "#333").text("✎");
    nodeGroups.each(function(d) {
      const group = d3.select(this);
      d.keyValuePairs.forEach((pair, i) => {
        const yPos = 48 + i * 22;
        const nodeWidth = d.width;
        const availableKeyWidth = Math.max(80, nodeWidth * 0.4);
        const availableValueWidth = Math.max(80, nodeWidth * 0.5);
        
        // Dynamic truncation based on available space
        const maxKeyChars = Math.floor(availableKeyWidth / 7); // Approximate char width
        const maxValueChars = Math.floor(availableValueWidth / 7);
        
        const truncatedKey = pair.key.length > maxKeyChars ? pair.key.substring(0, maxKeyChars - 3) + '...' : pair.key;
        const truncatedValue = String(pair.value).length > maxValueChars ? String(pair.value).substring(0, maxValueChars - 3) + '...' : String(pair.value);
        
        // Key text with tooltip
        const keyText = group.append("text")
          .attr("x", 15)
          .attr("y", yPos)
          .attr("font-family", "monospace")
          .attr("font-size", "12px")
          .attr("font-weight", "500")
          .attr("fill", "#333")
          .style("cursor", pair.key.length > maxKeyChars ? "help" : "default")
          .text(`${truncatedKey}:`);
        
        // Add tooltip for truncated keys
        if (pair.key.length > maxKeyChars) {
          keyText.append("title").text(pair.key);
        }
        
        // Value text with tooltip
        const valueText = group.append("text")
          .attr("x", Math.min(140, availableKeyWidth + 25))
          .attr("y", yPos)
          .attr("font-family", "monospace")
          .attr("font-size", "12px")
          .attr("fill", "#666")
          .style("cursor", String(pair.value).length > maxValueChars ? "help" : "default")
          .text(truncatedValue);
        
        // Add tooltip for truncated values
        if (String(pair.value).length > maxValueChars) {
          valueText.append("title").text(String(pair.value));
        }
      });
    });
    const bounds = container.node().getBBox();
    if (bounds.width > 0 && bounds.height > 0) {
      const scale = Math.min(width / bounds.width, height / bounds.height) * 0.9;
      const translate = [(width - bounds.width * scale) / 2 - bounds.x * scale, (height - bounds.height * scale) / 2 - bounds.y * scale];
      svg.call(zoom.transform, d3.zoomIdentity.translate(translate[0], translate[1]).scale(scale));
    }
  };

  const handleOpenModal = (node, mode) => {
    setActiveNode(node);
    setModalMode(mode);
    if (mode === 'edit') {
      const fields = node.keyValuePairs.map(pair => ({
        key: pair.key,
        value: pair.value,
        type: pair.type,
        originalKey: pair.key,
      }));
      setEditableFields(fields);
    }
    setModalOpened(true);
  };

  const handleFieldChange = (index, fieldName, value) => {
    const updatedFields = [...editableFields];
    updatedFields[index][fieldName] = value;
    setEditableFields(updatedFields);
  };

  // *** THIS FUNCTION HAS BEEN CORRECTED ***
  const handleSaveEdit = () => {
    if (!activeNode) return;
    
    const updatedFullData = JSON.parse(JSON.stringify(fullData));

    // Determine the base path of the current view.
    // If `data` (the current view) is the same as `fullData`, we are at the root.
    const isRootView = data === fullData;
    const basePath = isRootView ? 'root' : fileName;

    // The activeNode.path is always relative to the current view.
    // We construct the absolute path by joining the basePath and the relative node path.
    let absolutePath;
    if (activeNode.path === 'root') {
        // If we're editing the root of the current view, the absolute path is the view's path.
        absolutePath = basePath;
    } else {
        // Otherwise, combine the view path and the relative node path.
        const cleanRelativePath = activeNode.path.replace(/^root/, ''); // Removes 'root' but keeps '.users' or '[0]'
        absolutePath = basePath + cleanRelativePath;
    }

    const findObjectByPath = (obj, path) => {
      const pathParts = path.replace(/^root\.?/, '').match(/([a-zA-Z0-9_]+)|(\[\d+\])/g);
      if (!pathParts) return path === 'root' ? obj : undefined;
      let current = obj;
      for (const part of pathParts) {
        if (current === undefined) return undefined;
        if (part.startsWith('[')) {
          const index = parseInt(part.slice(1, -1));
          current = current[index];
        } else {
          current = current[part];
        }
      }
      return current;
    };

    // Find the target object within the full data structure using the absolute path
    const targetObject = findObjectByPath(updatedFullData, absolutePath);
    
    if (!targetObject) {
      showError('Could not find data to update. Path resolution failed.');
      return;
    }

    // Apply changes to the target object
    editableFields.forEach(field => {
      let convertedValue;
      switch (field.type) {
        case 'number': convertedValue = Number(field.value) || 0; break;
        case 'boolean': convertedValue = field.value.toLowerCase() === 'true'; break;
        default: convertedValue = field.value;
      }
      const key = field.key, originalKey = field.originalKey;
      if (Array.isArray(targetObject)) {
        const index = parseInt(originalKey.slice(1, -1));
        if (!isNaN(index)) targetObject[index] = convertedValue;
      } else {
        if (key !== originalKey && targetObject.hasOwnProperty(originalKey)) {
          delete targetObject[originalKey];
        }
        targetObject[key] = convertedValue;
      }
    });

    // Call the function from the parent to update the master state
    onUpdateData(updatedFullData);

    showSuccess(`Node '${activeNode.text}' updated.`);
    setModalOpened(false);
    setActiveNode(null);
  };

  const handleDownloadUpdatedJson = () => {
    if (!fullData || !fileName) return;
    
    const baseName = fileName.split('.')[0];
    const newFileName = `${baseName}_updated.json`;
    const blob = new Blob([JSON.stringify(fullData, null, 2)], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = newFileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);

    showSuccess(`Your browser will now prompt you to save ${newFileName}`);
  };

  const handleRecenter = () => {
    if (!svgRef.current || !zoomRef.current) return;
    const svg = d3.select(svgRef.current);
    const container = svg.select("g");
    if (container.node()) {
      const width = svg.node().parentElement.clientWidth;
      const height = svg.node().parentElement.clientHeight;
      const bounds = container.node().getBBox();
      if (bounds.width > 0 && bounds.height > 0) {
        const scale = Math.min(width / bounds.width, height / bounds.height) * 0.9;
        const translate = [(width - bounds.width * scale) / 2 - bounds.x * scale, (height - bounds.height * scale) / 2 - bounds.y * scale];
        const transform = d3.zoomIdentity.translate(translate[0], translate[1]).scale(scale);
        svg.transition().duration(500).call(zoomRef.current.transform, transform);
      }
    }
  };

  const handleZoomIn = () => svgRef.current && d3.select(svgRef.current).transition().call(zoomRef.current.scaleBy, 1.2);
  const handleZoomOut = () => svgRef.current && d3.select(svgRef.current).transition().call(zoomRef.current.scaleBy, 0.8);

  useImperativeHandle(ref, () => ({
    downloadAsSVG: async () => {
      const svgElement = svgRef.current;
      if (!svgElement) return null;
      
      // Create a clone of the SVG to avoid modifying the original
      const clone = svgElement.cloneNode(true);
      
      // Add XML namespace if not present
      if (!clone.getAttribute('xmlns')) {
        clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      }
      
      // Serialize the SVG to a string
      const serializer = new XMLSerializer();
      let svgString = serializer.serializeToString(clone);
      
      // Add XML declaration and SVG DOCTYPE
      svgString = '<?xml version="1.0" standalone="no"?>\r\n' + svgString;
      
      // Create a blob with the SVG data
      const svgBlob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
      return svgBlob;
    },
    downloadAsImage: async (type = 'png') => {
      const svgElement = svgRef.current;
      if (!svgElement) return null;
      
      return new Promise((resolve) => {
        try {
          // Get the SVG as a string
          const serializer = new XMLSerializer();
          const svgString = serializer.serializeToString(svgElement);
          
          // Create a canvas element
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          
          // Set canvas dimensions to match SVG
          canvas.width = svgElement.width.baseVal.value;
          canvas.height = svgElement.height.baseVal.value;
          
          // Create an image element
          const img = new Image();
          const svgBlob = new Blob([svgString], {type: 'image/svg+xml;charset=utf-8'});
          const url = URL.createObjectURL(svgBlob);
          
          img.onload = function() {
            // Draw the SVG image to the canvas
            ctx.drawImage(img, 0, 0);
            URL.revokeObjectURL(url);
            
            // Convert canvas to blob
            canvas.toBlob((blob) => {
              resolve(blob);
            }, `image/${type}`, 1);
          };
          
          img.onerror = function() {
            console.error('Error loading SVG image');
            resolve(null);
          };
          
          img.src = url;
        } catch (error) {
          console.error('Error generating image:', error);
          resolve(null);
        }
      });
    },
    downloadAsPDF: async () => {
      const svgElement = svgRef.current;
      if (!svgElement) return null;
      
      return new Promise((resolve) => {
        try {
          // Get the SVG as a string
          const serializer = new XMLSerializer();
          const svgString = serializer.serializeToString(svgElement);
          
          // Create a canvas element
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          
          // Set canvas dimensions to match SVG
          canvas.width = svgElement.width.baseVal.value;
          canvas.height = svgElement.height.baseVal.value;
          
          // Create an image element
          const img = new Image();
          const svgBlob = new Blob([svgString], {type: 'image/svg+xml;charset=utf-8'});
          const url = URL.createObjectURL(svgBlob);
          
          img.onload = async function() {
            try {
              // Draw the SVG image to the canvas
              ctx.drawImage(img, 0, 0);
              URL.revokeObjectURL(url);
              
              // Create PDF
              const imgData = canvas.toDataURL('image/png');
              const pdf = new jsPDF({
                orientation: 'landscape',
                unit: 'mm'
              });
              
              const imgProps = pdf.getImageProperties(imgData);
              const pdfWidth = pdf.internal.pageSize.getWidth();
              const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
              
              pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
              resolve(pdf.output('blob'));
            } catch (error) {
              console.error('Error generating PDF:', error);
              resolve(null);
            }
          };
          
          img.onerror = function() {
            console.error('Error loading SVG image for PDF');
            resolve(null);
          };
          
          img.src = url;
        } catch (error) {
          console.error('Error in PDF generation:', error);
          resolve(null);
        }
      });
    }
  }));

  return (
    <div className="h-full flex flex-col">
      <div className="flex justify-between items-center mb-4">
        <div className="flex items-center gap-2">
          <button 
            className="px-2 py-1 text-xs bg-gray-100 hover:bg-gray-200 rounded disabled:opacity-50 disabled:cursor-not-allowed"
            onClick={handleZoomOut} 
            disabled={zoomLevel <= 0.2}
          >
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 12H4" />
            </svg>
          </button>
          <span className="text-sm text-gray-500 w-10 text-center">{Math.round(zoomLevel * 100)}%</span>
          <button 
            className="px-2 py-1 text-xs bg-gray-100 hover:bg-gray-200 rounded disabled:opacity-50 disabled:cursor-not-allowed"
            onClick={handleZoomIn} 
            disabled={zoomLevel >= 4}
          >
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
            </svg>
          </button>
          <button 
            className="px-2 py-1 text-xs bg-gray-100 hover:bg-gray-200 rounded"
            onClick={handleRecenter} 
            title="Recenter Diagram"
          >
            <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </button>
        </div>
      </div>

      <div className="flex-1 bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
        <svg ref={svgRef} className="w-full h-full" style={{ backgroundColor: '#fdfdfd' }} />
      </div>

      {modalOpened && (
        <div className="fixed inset-0 bg-opacity-10 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg shadow-xl max-w-2xl w-full mx-4 max-h-[80vh] overflow-hidden">
            <div className="flex items-center gap-2 p-4 border-b border-gray-200">
              {modalMode === 'view' ? (
                <svg className="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              ) : (
                <svg className="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              )}
              <h3 className="text-lg font-semibold text-gray-800">
                {modalMode === 'view' ? 'View' : 'Edit'} Properties for: {activeNode?.text}
              </h3>
            </div>
            
            <div className="p-4 max-h-96 overflow-y-auto">
              {modalMode === 'edit' ? (
                <div className="space-y-4">
                  {editableFields.length > 0 ? editableFields.map((field, index) => (
                    <div key={field.originalKey} className="border border-gray-200 rounded-lg p-3">
                      <div className="space-y-3">
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">Key</label>
                          <input 
                            type="text"
                            value={field.key} 
                            onChange={(e) => handleFieldChange(index, 'key', e.target.value)} 
                            disabled={field.originalKey.startsWith('[')}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
                          />
                        </div>
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">Value</label>
                          <textarea 
                            value={field.value} 
                            onChange={(e) => handleFieldChange(index, 'value', e.target.value)} 
                            rows={2}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 resize-y"
                          />
                        </div>
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">Data Type</label>
                          <select 
                            value={field.type} 
                            onChange={(e) => handleFieldChange(index, 'type', e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                          >
                            <option value="string">string</option>
                            <option value="number">number</option>
                            <option value="boolean">boolean</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  )) : (
                    <p className="text-gray-500">This node has no directly editable properties.</p>
                  )}
                </div>
              ) : (
                <div className="space-y-3">
                  {activeNode?.keyValuePairs.length > 0 ? activeNode.keyValuePairs.map(pair => (
                    <div key={pair.key} className="border border-gray-200 rounded-lg p-3">
                      <div className="grid grid-cols-2 gap-4">
                        <span className="font-medium text-gray-700">{pair.key}:</span>
                        <span className="text-gray-600">{pair.value}</span>
                      </div>
                    </div>
                  )) : (
                    <p className="text-gray-500">This node has no viewable properties.</p>
                  )}
                </div>
              )}
            </div>
            
            <div className="flex justify-end gap-2 p-4 border-t border-gray-200">
              <button 
                className="px-4 py-2 text-sm bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-md"
                onClick={() => setModalOpened(false)}
              >
                {modalMode === 'view' ? 'Close' : 'Cancel'}
              </button>
              {modalMode === 'edit' && (
                <button 
                  className="px-4 py-2 text-sm bg-blue-600 hover:bg-blue-700 text-white rounded-md disabled:opacity-50 disabled:cursor-not-allowed"
                  onClick={handleSaveEdit} 
                  disabled={editableFields.length === 0}
                >
                  Save Changes
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
});

export default DiagramCanvas;
