from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Paris Smart Mobility",
    description="Assistant IA pour la mobilité parisienne",
    version="0.1.0"
)

# Router principal
router = APIRouter()

# Configuration CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@router.get("/health")
async def health_check():
    """Basic health check."""
    return {"status": "healthy", "service": "Paris Smart Mobility"}

@router.get("/")
async def root():
    """Root endpoint."""
    return {
        "project": "Paris Smart Mobility",
        "author": "comlami",  # Replace!
        "status": "In Development"
    }

# On inclut notre router
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)