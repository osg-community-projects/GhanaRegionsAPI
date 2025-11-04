from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models.district import District, DistrictWithTowns
from app.services.district_service import DistrictService

router = APIRouter()

@router.get("/districts", response_model=List[District])
async def get_all_districts():
    """Get all districts in Ghana"""
    return DistrictService.get_all_districts()

@router.get("/districts/{district_id}", response_model=District)
async def get_district_by_id(district_id: int):
    """Get a specific district by ID"""
    district = DistrictService.get_district_by_id(district_id)
    if not district:
        raise HTTPException(status_code=404, detail="District not found")
    return district

@router.get("/districts/{district_id}/details", response_model=DistrictWithTowns)
async def get_district_with_towns(district_id: int):
    """Get a district with all its towns"""
    district = DistrictService.get_district_with_towns(district_id)
    if not district:
        raise HTTPException(status_code=404, detail="District not found")
    return district

@router.get("/regions/{region_id}/districts", response_model=List[District])
async def get_districts_by_region(region_id: int):
    """Get all districts in a specific region"""
    districts = DistrictService.get_districts_by_region(region_id)
    if not districts:
        raise HTTPException(status_code=404, detail="No districts found for this region")
    return districts

@router.get("/districts/search", response_model=List[District])
async def search_districts(q: str = Query(..., description="Search query for district name")):
    """Search districts by name"""
    return DistrictService.search_districts(q)
