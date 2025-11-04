from typing import List, Optional
from app.models.district import District, DistrictWithTowns
from app.models.town import Town
from app.database.data import DISTRICTS_DATA, TOWNS_DATA

class DistrictService:
    @staticmethod
    def get_all_districts() -> List[District]:
        return [District(**district) for district in DISTRICTS_DATA]
    
    @staticmethod
    def get_district_by_id(district_id: int) -> Optional[District]:
        for district_data in DISTRICTS_DATA:
            if district_data["id"] == district_id:
                return District(**district_data)
        return None
    
    @staticmethod
    def get_districts_by_region(region_id: int) -> List[District]:
        return [
            District(**district) 
            for district in DISTRICTS_DATA 
            if district["region_id"] == region_id
        ]
    
    @staticmethod
    def get_district_with_towns(district_id: int) -> Optional[DistrictWithTowns]:
        district_data = None
        for d in DISTRICTS_DATA:
            if d["id"] == district_id:
                district_data = d
                break
        
        if not district_data:
            return None
        
        # Get towns for this district
        towns = [
            Town(**town) 
            for town in TOWNS_DATA 
            if town["district_id"] == district_id
        ]
        
        return DistrictWithTowns(
            **district_data,
            towns=towns
        )
    
    @staticmethod
    def search_districts(query: str) -> List[District]:
        results = []
        query_lower = query.lower()
        
        for district_data in DISTRICTS_DATA:
            if query_lower in district_data["name"].lower():
                results.append(District(**district_data))
        
        return results
