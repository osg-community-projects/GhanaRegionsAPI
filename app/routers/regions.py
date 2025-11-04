from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.region import Region, RegionWithDistricts
from app.services.region_service import RegionService

router = APIRouter()

@router.get("/regions", response_model=List[Region])
async def get_all_regions():
    """Get all regions in Ghana"""
    return RegionService.get_all_regions()

@router.get("/regions/{region_id}", response_model=Region)
async def get_region_by_id(region_id: int):
    """Get a specific region by ID"""
    region = RegionService.get_region_by_id(region_id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.get("/regions/{region_id}/details", response_model=RegionWithDistricts)
async def get_region_with_districts(region_id: int):
    """Get a region with all its districts"""
    region = RegionService.get_region_with_districts(region_id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.get("/regions/name/{region_name}", response_model=Region)
async def get_region_by_name(region_name: str):
    """Get a region by name"""
    region = RegionService.get_region_by_name(region_name)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.get("/regions/search", response_model=List[Region])
async def search_regions(q: str = Query(..., description="Search query for region name or capital")):
    """Search regions by name or capital"""
    return RegionService.search_regions(q)
