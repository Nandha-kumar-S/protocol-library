// components/JsonTreeView.js
import { useState } from 'react';

// This is a single node in the tree
const TreeNode = ({ nodeKey, nodeValue, onNodeSelect, path, selectedPath, onPathSelect }) => {
  const [isOpen, setIsOpen] = useState(true);
  const isObject = typeof nodeValue === 'object' && nodeValue !== null && !Array.isArray(nodeValue);
  const isArray = Array.isArray(nodeValue);

  // MODIFIED: Correctly handles the initial empty path for the root node
  const currentPath = path ? `${path}.${nodeKey}` : nodeKey;
  const isSelected = selectedPath === currentPath;

  const handleToggle = (e) => {
    e.stopPropagation();
    setIsOpen((prev) => !prev);
  };

  const handleVisualize = (e) => {
    e.stopPropagation();
    onNodeSelect(nodeValue, currentPath);
    onPathSelect(currentPath);
  };

  if (!isObject && !isArray) {
    // Render a simple key-value pair for primitives
    return (
      <div className="flex items-center gap-2 pl-4 py-1">
        <span className="text-sm font-medium text-gray-700">{nodeKey}:</span>
        <span className="text-sm text-gray-500">{String(nodeValue)}</span>
      </div>
    );
  }

  return (
    <div className="mb-1">
      <div
        className={`flex items-center gap-2 cursor-pointer select-none p-1 rounded transition-colors ${
          isSelected
            ? 'bg-blue-100 border border-blue-300'
            : 'hover:bg-gray-50'
        }`}
        onClick={handleToggle}
      >
        {isOpen ? (
          <svg className="w-3 h-3 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        ) : (
          <svg className="w-3 h-3 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        )}
        <span className="text-sm font-semibold text-gray-800">{nodeKey}</span>
        <span className="text-xs text-gray-400">
          {isArray ? `[${nodeValue.length}]` : `{${Object.keys(nodeValue).length}}`}
        </span>
        <button
          onClick={handleVisualize}
          className={`ml-auto p-1 rounded transition-colors ${
            isSelected
              ? 'text-blue-800 bg-blue-200 hover:bg-blue-300'
              : 'text-blue-600 hover:text-blue-800 hover:bg-blue-50'
          }`}
          title="Visualize this node"
        >
          <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
          </svg>
        </button>
      </div>
      {isOpen && (
        <div className="pl-4 border-l border-gray-200 ml-2">
          {isArray ? (
            nodeValue.map((item, index) => (
              <TreeNode
                key={index}
                nodeKey={`[${index}]`}
                nodeValue={item}
                onNodeSelect={onNodeSelect}
                // MODIFIED: Pass the newly built path down
                path={currentPath}
                selectedPath={selectedPath}
                onPathSelect={onPathSelect}
              />
            ))
          ) : (
            Object.entries(nodeValue).map(([key, value]) => (
              <TreeNode
                key={key}
                nodeKey={key}
                nodeValue={value}
                onNodeSelect={onNodeSelect}
                // MODIFIED: Pass the newly built path down
                path={currentPath}
                selectedPath={selectedPath}
                onPathSelect={onPathSelect}
              />
            ))
          )}
        </div>
      )}
    </div>
  );
};

// This is the main component that starts the tree rendering
export default function JsonTreeView({ data, onNodeSelect }) {
  const [selectedPath, setSelectedPath] = useState(null);

  if (!data) {
    return (
      <div className="text-center text-gray-500 text-sm">
        Select a file to see its JSON structure.
      </div>
    );
  }
  
  return (
    <div className="space-y-1">
      <TreeNode
        key="root"
        nodeKey="root"
        nodeValue={data}
        onNodeSelect={onNodeSelect}
        path=""
        selectedPath={selectedPath}
        onPathSelect={setSelectedPath}
      />
    </div>
  );
}