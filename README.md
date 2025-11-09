# Protocol Library: AI-Powered Protocol Standardization

## 1. Project Description

The Protocol Library is a full-stack application designed to solve a critical bottleneck in the clinical trial industry. It leverages AI to automatically parse unstructured clinical trial protocol documents and convert them into the **CDISC USDM (Universal Study Definition Model)**, a globally recognized, machine-readable standard.

This creates a "digital twin" of the protocol, enabling downstream automation, improving data quality, and accelerating the entire clinical trial lifecycle.

### Key Features
*   **AI-Powered Pipeline:** A Python backend that uses Large Language Models (LLMs) to extract, standardize, and connect protocol information.
*   **Human-in-the-Loop Validation:** An intuitive user interface for experts to review and approve AI-generated content, ensuring accuracy.
*   **Interactive Jobs Dashboard:** A React-based frontend to upload documents, monitor job progress in real-time, and manage the entire workflow.

---

## 2. Technologies & Libraries

### Backend
*   **Language:** Python
*   **AI/ML:** OpenAI, LangChain
*   **PDF Processing:** PyMuPDF, pdfplumber

### Frontend
*   **Framework:** React
*   **Language:** JavaScript
*   **API Communication:** Axios

---

## 3. Running the Project Locally

To run this project, you will need to start both the backend server and the frontend development server.

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r ../requirements.txt
    ```

4.  **Configure Environment Variables (IMPORTANT):**
    The current `backend/ml/config/llm_models.yaml` file contains hardcoded API keys. This is a security risk. It is strongly recommended to remove them and use environment variables.

    Create a `.env` file in the `backend` directory and add your keys:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    AZURE_API_ENDPOINT=your_azure_endpoint_here
    ```

5.  **Run the server:**
    *(You may need to update this command based on your entry point file, e.g., `main.py`)*
    ```bash
    # Example for FastAPI
    uvicorn main:app --reload
    
    # Example for Flask
    flask run
    ```

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the development server:**
    ```bash
    npm start
    ```

Once both servers are running, you can access the application at `http://localhost:3000` (or the port specified by the React development server).
