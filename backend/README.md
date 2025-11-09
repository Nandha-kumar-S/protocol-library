# Protocol Library Backend

FastAPI backend service for managing and analyzing clinical trial protocols using CDISC USDM standards. This service handles protocol PDF processing, data extraction, and USDM-compliant data management.

## Prerequisites

- Python 3.12 or higher
- PostgreSQL database

## Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── core/               # Core configurations and settings
├── modules/            # Feature modules (dashboard, jobs, search)
│   ├── dashboard/      # Dashboard related endpoints
│   ├── jobs/          # Job processing and management
│   └── search/        # Search functionality
└── db/                # Database models and mock data
```

## Setup Instructions

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install ml dependencies:
   ```bash
   pip install -r ml/requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the backend directory with the following content:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/protocol_library
   ```

5. Set up the llm_models.yaml:
   Create a `llm_models.yaml` file inside the ml/config/ in the backend directory with the following content:
   ```
   common_azure_config: 
   api_key: 
   api_endpoint:

   CHOSEN_MODEL:
   MODE: 'request'

   OPENAI_GPTO3:
   <<: *common_azure_config
   api_version: 
   deployment_name: 

   OPENAI_GPTO3_MINI:
   <<: *common_azure_config
   api_version:
   deployment_name:

   OPENAI_GPT5:
   <<: *common_azure_config
   api_version:
   deployment_name:

   OPENAI_GPT5_MINI:
   <<: *common_azure_config
   api_version:
   deployment_name:

   OPENAI_GPT4O_MINI:
   api_key: 
   api_endpoint:
   ```

6. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at http://localhost:8000

7. Navigate to http://localhost:8000/docs to see the list of APIs

## API Endpoints

The backend provides the following main endpoints:

- `POST /api/jobs/upload` - Upload protocol PDFs for processing
- `GET /api/jobs/{job_id}` - Get job status and details
- `GET /api/dashboard/stats` - Get dashboard statistics
- `GET /api/search` - Search through processed protocols

For a complete list of endpoints and their documentation, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Module Structure
Each feature module follows a consistent structure:
- `models.py` - Data models and schemas
- `router.py` - API route definitions
- `service.py` - Business logic implementation

### Testing
To run the tests:
```bash
pytest
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## License

This project is licensed under the MIT License.