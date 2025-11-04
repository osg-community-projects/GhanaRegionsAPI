from typing import List, Optional
from app.models.region import Region, RegionWithDistricts
from app.models.district import District
from app.database.data import REGIONS_DATA, DISTRICTS_DATA

class RegionService:
    @staticmethod
    def get_all_regions() -> List[Region]:
        return [Region(**region) for region in REGIONS_DATA]
    
    @staticmethod
    def get_region_by_id(region_id: int) -> Optional[Region]:
        for region_data in REGIONS_DATA:
            if region_data["id"] == region_id:
                return Region(**region_data)
        return None
    
    @staticmethod
    def get_region_by_name(name: str) -> Optional[Region]:
        for region_data in REGIONS_DATA:
            if region_data["name"].lower() == name.lower():
                return Region(**region_data)
        return None
    
    @staticmethod
    def get_region_with_districts(region_id: int) -> Optional[RegionWithDistricts]:
        region_data = None
        for r in REGIONS_DATA:
            if r["id"] == region_id:
                region_data = r
                break
        
        if not region_data:
            return None
        
        # Get districts for this region
        districts = [
            District(**district) 
            for district in DISTRICTS_DATA 
            if district["region_id"] == region_id
        ]
        
        return RegionWithDistricts(
            **region_data,
            districts=districts
        )
    
    @staticmethod
    def search_regions(query: str) -> List[Region]:
        results = []
        query_lower = query.lower()
        
        for region_data in REGIONS_DATA:
            if (query_lower in region_data["name"].lower() or 
                query_lower in region_data["capital"].lower()):
                results.append(Region(**region_data))
        
        return results
