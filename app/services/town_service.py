from typing import List, Optional
from app.models.town import Town
from app.database.data import TOWNS_DATA

class TownService:
    @staticmethod
    def get_all_towns() -> List[Town]:
        return [Town(**town) for town in TOWNS_DATA]
    
    @staticmethod
    def get_town_by_id(town_id: int) -> Optional[Town]:
        for town_data in TOWNS_DATA:
            if town_data["id"] == town_id:
                return Town(**town_data)
        return None
    
    @staticmethod
    def get_towns_by_district(district_id: int) -> List[Town]:
        return [
            Town(**town) 
            for town in TOWNS_DATA 
            if town["district_id"] == district_id
        ]
    
    @staticmethod
    def get_towns_by_population_range(min_pop: int, max_pop: int) -> List[Town]:
        return [
            Town(**town) 
            for town in TOWNS_DATA 
            if town.get("population") and min_pop <= town["population"] <= max_pop
        ]
    
    @staticmethod
    def search_towns(query: str) -> List[Town]:
        results = []
        query_lower = query.lower()
        
        for town_data in TOWNS_DATA:
            if query_lower in town_data["name"].lower():
                results.append(Town(**town_data))
        
        return results
    
    @staticmethod
    def get_largest_towns(limit: int = 10) -> List[Town]:
        towns_with_pop = [
            Town(**town) 
            for town in TOWNS_DATA 
            if town.get("population")
        ]
        return sorted(towns_with_pop, key=lambda x: x.population, reverse=True)[:limit]
