# Protocol Library

A modern React-based Protocol Library application for managing research protocols, studies, and analysis jobs.

## Tech Stack

- **React 18** - Modern React with hooks and functional components
- **React Router v6** - Client-side routing and navigation
- **Redux Toolkit** - State management with modern Redux patterns
- **Axios** - HTTP client for API requests
- **Styled Components** - CSS-in-JS styling with interactive designs
- **Monaco Editor** - Advanced JSON editor for protocol configurations
- **React Icons** - Comprehensive icon library
- **Vite** - Fast build tool and development server

## Features

### Core Functionality
- ✅ **Protocol Management** - Create, read, update, and delete research protocols
- ✅ **Study Management** - Manage research studies with participant tracking
- ✅ **Job Monitoring** - Track analysis jobs with real-time status updates
- ✅ **JSON Editor** - Advanced JSON editor for protocol configurations
- ✅ **Delete Functionality** - Confirmation dialogs for safe deletion
- ✅ **Study Selection** - When a study is selected, all related pages are displayed
- ✅ **Fullscreen Support** - Toggle fullscreen mode for better focus
- ✅ **Polling System** - Automatic status updates for in-progress jobs

### User Interface
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Clean, professional interface with interactive elements
- 🌈 **Styled Components** - Consistent styling with hover effects and animations
- 📊 **Dashboard** - Overview of protocols, studies, and job statistics
- 🔍 **Search & Filter** - Find protocols, studies, and jobs quickly

### Technical Features
- 🔄 **Redux State Management** - Centralized state with async actions
- 🌐 **API Integration** - RESTful API calls with error handling
- 📝 **Mock Data** - Built-in mock data for development and testing
- ⚡ **Real-time Updates** - Polling service for job status updates
- 🛡️ **Error Handling** - Comprehensive error handling and user feedback

## Getting Started

### Prerequisites
- Node.js (v20 or higher)
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd protocol-library/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000` to view the application.

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── DeleteButton/    # Confirmation delete button
│   ├── FullscreenProvider/ # Fullscreen context provider
│   ├── JsonEditor/      # Monaco-based JSON editor
│   └── Layout/          # Main layout components
├── data/               # Mock data for testing
├── pages/              # Page components
│   ├── Dashboard.jsx   # Main dashboard
│   ├── Protocols.jsx   # Protocol management
│   ├── Studies.jsx     # Study management
│   ├── StudyDetail.jsx # Study detail view
│   ├── Jobs.jsx        # Job monitoring
│   └── NotFound.jsx    # 404 page
├── services/           # API and external services
│   ├── api.js          # API client configuration
│   └── polling.js      # Job polling service
├── store/              # Redux store configuration
│   ├── store.js        # Store setup
│   └── slices/         # Redux slices
└── App.jsx             # Main application component
```

## API Configuration

The application supports both mock data and real API endpoints:

- **Mock Mode** (default): Uses built-in mock data for development
- **API Mode**: Configure `REACT_APP_API_URL` environment variable

To switch to real API:
1. Set `USE_MOCK_API = false` in `src/services/api.js`
2. Configure your API endpoint in `.env`:
   ```
   REACT_APP_API_URL=http://your-api-server.com/api
   ```

## Key Features Explained

### Protocol Management
- Create new protocols with JSON configuration
- Edit existing protocols using the built-in JSON editor
- Delete protocols with confirmation dialogs
- Search and filter protocols

### Study Management
- Create studies with participant information
- View study details with related pages
- Navigate between studies and their associated data
- Track study progress and statistics

### Job Monitoring
- View all analysis jobs with status indicators
- Automatic polling for in-progress jobs
- Manual refresh capabilities
- Filter jobs by status (pending, in-progress, completed, failed)

### JSON Editor
- Syntax highlighting and validation
- Auto-formatting and error detection
- Save/reset functionality
- Full-screen editing mode

## Development Notes

### Mock Data
The application includes comprehensive mock data in `src/data/mockData.js`:
- Sample protocols with realistic configurations
- Study data with participant information
- Job data with various statuses
- Related pages for studies

### Polling System
The polling service automatically monitors in-progress jobs:
- Configurable polling intervals
- Automatic start/stop based on job status
- Manual control for individual jobs
- Efficient resource management

### State Management
Redux Toolkit is used for state management:
- Separate slices for protocols, studies, and jobs
- Async thunks for API calls
- Centralized error handling
- Optimistic updates where appropriate

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
