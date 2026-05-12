import logging
from datetime import datetime
from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import signal
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
import os
from .routes import auth, staffs

app = FastAPI(title="Unity POC")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/check")
async def check():
    return 204

app.include_router(auth.router, prefix='/auth', tags=['Auth'])
app.include_router(staffs.router, prefix='/staffs', tags= ['Staffs'])

# Get the absolute path of the 'storage' directory (one level above 'backend')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current file's directory
storage_dir = os.path.abspath(os.path.join(BASE_DIR, "../../storage"))

if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)  # Ensure directory exists

# Mount static files with the correct path
app.mount("/storage", StaticFiles(directory=storage_dir), name="storage")


# Trusted Host Middleware (Security)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])  # Change for production

# Graceful Shutdown Handling
@app.on_event("shutdown")
async def shutdown():
    # logger.info("Shutting down gracefully...")
    pass

# Signal Handling
def shutdown_signal(signal_number, frame):
    # logger.warning("Received signal %s. Initiating shutdown...", signal_number)
    asyncio.create_task(shutdown())  # Gracefully shutdown instead of force exit

signal.signal(signal.SIGINT, shutdown_signal)
signal.signal(signal.SIGTERM, shutdown_signal)
