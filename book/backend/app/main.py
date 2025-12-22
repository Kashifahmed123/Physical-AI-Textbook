from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from . import models
from .database import engine
from .routes import chatbot, auth, content

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database
    models.Base.metadata.create_all(bind=engine)
    logger.info("Database initialized")
    yield
    # Clean up if needed
    logger.info("Application shutdown")

app = FastAPI(
    title="Physical AI & Humanoid Robotics Textbook API",
    description="API for the AI-Native Technical Textbook",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chatbot.router, prefix="/api/v1", tags=["chatbot"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(content.router, prefix="/api/v1", tags=["content"])

@app.get("/")
def read_root():
    return {"message": "Physical AI & Humanoid Robotics Textbook API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}