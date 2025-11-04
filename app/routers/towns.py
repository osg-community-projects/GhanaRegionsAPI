from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models.town import Town
from app.services.town_service import TownService

router = APIRouter()

@router.get("/towns", response_model=List[Town])
async def get_all_towns():
    """Get all towns in Ghana"""
    return TownService.get_all_towns()

@router.get("/towns/{town_id}", response_model=Town)
async def get_town_by_id(town_id: int):
    """Get a specific town by ID"""
    town = TownService.get_town_by_id(town_id)
    if not town:
        raise HTTPException(status_code=404, detail="Town not found")
    return town

@router.get("/districts/{district_id}/towns", response_model=List[Town])
async def get_towns_by_district(district_id: int):
    """Get all towns in a specific district"""
    towns = TownService.get_towns_by_district(district_id)
    if not towns:
        raise HTTPException(status_code=404, detail="No towns found for this district")
    return towns

@router.get("/towns/search", response_model=List[Town])
async def search_towns(q: str = Query(..., description="Search query for town name")):
    """Search towns by name"""
    return TownService.search_towns(q)

@router.get("/towns/largest", response_model=List[Town])
async def get_largest_towns(limit: int = Query(10, ge=1, le=50, description="Number of towns to return")):
    """Get the largest towns by population"""
    return TownService.get_largest_towns(limit)

@router.get("/towns/population", response_model=List[Town])
async def get_towns_by_population_range(
    min_pop: int = Query(..., ge=0, description="Minimum population"),
    max_pop: int = Query(..., ge=0, description="Maximum population")
):
    """Get towns within a population range"""
    if min_pop > max_pop:
        raise HTTPException(status_code=400, detail="Minimum population cannot be greater than maximum population")
    return TownService.get_towns_by_population_range(min_pop, max_pop)
