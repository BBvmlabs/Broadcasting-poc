# Broadcasting POC

A modern full-stack application's POC for network video broadcasting using FastAPI and WebSocket with a React frontend. Telecasting enables real-time video transmission across network infrastructure with a responsive user interface.

## 🎯 Features

- **Real-time Video Broadcasting**: Stream videos across the network using WebSocket technology
- **FastAPI Backend**: High-performance Python backend with async support
- **React Frontend**: Modern, responsive UI built with React 19 and Vite
- **Authentication & Authorization**: Built-in user authentication and staff management
- **CORS Enabled**: Cross-Origin Resource Sharing configured for seamless frontend-backend communication
- **Static File Management**: Integrated storage system for video and media files
- **Bootstrap Styling**: Professional UI with Bootstrap 5.3 integration

## 📋 Tech Stack

### Backend
- **FastAPI** (v0.95-0.110): Modern web framework for building APIs
- **Uvicorn** (v0.23-0.24): ASGI server for running FastAPI applications
- **SQLAlchemy** (v1.4-2.0): SQL toolkit and Object-Relational Mapping (ORM)
- **Python 3.x**: Backend runtime environment

### Frontend
- **React** (v19.1.0): JavaScript library for building user interfaces
- **React DOM** (v19.1.0): React package for working with the DOM
- **Vite** (v6.3.5): Next-generation frontend build tool
- **Bootstrap** (v5.3.6): CSS framework for responsive design
- **React Bootstrap** (v2.10.9): Bootstrap components as React components
- **Axios** (v1.9.0): HTTP client for API requests
- **ESLint**: JavaScript linter for code quality

## 📁 Project Structure

```
Telecasting/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI application entry point
│   │   ├── api/
│   │   │   ├── auth/               # Authentication endpoints
│   │   │   │   ├── login.py
│   │   │   │   └── signup.py
│   │   │   └── staff/              # Staff management endpoints
│   │   │       └── staff_creation.py
│   │   ├── routes/
│   │   │   ├── auth.py             # Auth router
│   │   │   └── staffs.py           # Staff router
│   │   ├── model/                  # Database models
│   │   ├── schema/                 # Pydantic schemas
│   │   ├── database/               # Database configuration
│   │   └── utils/                  # Utility functions
│   └── requirments.txt             # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── main.jsx                # React entry point
│   │   ├── App.jsx                 # Main App component
│   │   ├── App.css                 # App styling
│   │   ├── index.css               # Global styles
│   │   ├── pages/
│   │   │   └── login/              # Login page component
│   │   └── assets/                 # Static assets
│   ├── public/                     # Public static files
│   ├── index.html                  # HTML template
│   ├── package.json                # Frontend dependencies
│   ├── vite.config.js              # Vite configuration
│   └── eslint.config.js            # ESLint configuration
├── package.json                    # Root dependencies
├── package-lock.json
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- **Python** 3.8 or higher
- **Node.js** 16 or higher
- **npm** or **yarn** package manager

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirments.txt
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

The backend API will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs` (Swagger UI)

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Build for production:
   ```bash
   npm run build
   ```

The frontend will be available at `http://localhost:5173` (default Vite port)

## 📡 API Endpoints

### Authentication Routes
- **POST** `/auth/login` - User login
- **POST** `/auth/signup` - User registration

### Staff Management Routes
- **GET/POST** `/staffs/` - Staff management operations

### Health Check
- **GET** `/check` - Server health check endpoint (returns 204 No Content)

## 🔧 Configuration

### CORS Configuration
The backend has CORS enabled for all origins, methods, and headers (configured for development). For production, update the `CORSMiddleware` configuration in `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specify allowed domains
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

### Storage Directory
The application automatically creates and manages a `storage` directory at the root level for static files and video content.

## 🔐 Security Features

- **CORS Middleware**: Configured for cross-origin requests
- **Trusted Host Middleware**: Security layer for trusted hosts (update for production)
- **HTTPS Support**: Ready for SSL/TLS configuration
- **Graceful Shutdown**: Proper signal handling for clean application termination

## 📝 Development Scripts

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint code quality checks
- `npm run preview` - Preview production build locally

### Backend
- `uvicorn app.main:app --reload` - Run with auto-reload for development
- `uvicorn app.main:app` - Run production server

## 🐛 Debugging

### Backend
Access the interactive API documentation at `http://localhost:8000/docs` for testing endpoints.

### Frontend
- Browser DevTools for React component debugging
- Vite provides fast refresh for development
- ESLint helps maintain code quality

## 📦 Dependencies

See `backend/requirments.txt` and `frontend/package.json` for complete dependency lists with specific versions.

**Happy Broadcasting! 🎬**
