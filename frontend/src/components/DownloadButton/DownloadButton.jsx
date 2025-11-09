import React from 'react';
import { Menu } from '@headlessui/react';
import { FiDownload } from 'react-icons/fi';

const DownloadButton = ({ onDownload }) => {
  const downloadOptions = [
    { format: 'SVG', type: 'image/svg+xml', extension: 'svg' },
    { format: 'PDF', type: 'application/pdf', extension: 'pdf' },
    { format: 'JPG', type: 'image/jpeg', extension: 'jpg' },
  ];

  return (
    <Menu as="div" className="relative inline-block text-left">
      <div>
        <Menu.Button
          className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors duration-200 focus:outline-none"
          title="Download Diagram"
        >
          <FiDownload className="w-5 h-5" />
        </Menu.Button>
      </div>
      <Menu.Items className="absolute right-0 w-36 mt-2 origin-top-right bg-white divide-y divide-gray-100 rounded-md shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none z-50">
        <div className="px-1 py-1">
          {downloadOptions.map((option) => (
            <Menu.Item key={option.extension}>
              {({ active }) => (
                <button
                  onClick={() => onDownload(option.extension)}
                  className={`${active ? 'bg-blue-500 text-white' : 'text-gray-900'
                    } group flex rounded-md items-center w-full px-2 py-2 text-sm`}
                >
                  {option.format}
                </button>
              )}
            </Menu.Item>
          ))}
        </div>
      </Menu.Items>
    </Menu>
  );
};

export default DownloadButton;
