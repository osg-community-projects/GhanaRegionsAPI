from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import regions, districts, towns

app = FastAPI(
    title="Ghana Regions API",
    description="A comprehensive API for Ghana's regions, districts, and towns",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(regions.router, prefix="/api/v1", tags=["regions"])
app.include_router(districts.router, prefix="/api/v1", tags=["districts"])
app.include_router(towns.router, prefix="/api/v1", tags=["towns"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Ghana Regions API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
