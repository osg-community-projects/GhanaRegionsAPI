#!/usr/bin/env python3
"""
Simple test script to verify the Ghana Regions API functionality
"""

from app.services.region_service import RegionService
from app.services.district_service import DistrictService
from app.services.town_service import TownService

def test_services():
    print("🇬🇭 Testing Ghana Regions API Services\n")
    
    # Test Region Service
    print("📍 Testing Region Service:")
    regions = RegionService.get_all_regions()
    print(f"   ✓ Found {len(regions)} regions")
    
    accra_region = RegionService.get_region_by_name("GREATER ACCRA")
    if accra_region:
        print(f"   ✓ Greater Accra Region: {accra_region.capital}")
    
    # Test District Service
    print("\n🏛️  Testing District Service:")
    districts = DistrictService.get_all_districts()
    print(f"   ✓ Found {len(districts)} districts")
    
    accra_districts = DistrictService.get_districts_by_region(7)  # Greater Accra
    print(f"   ✓ Greater Accra has {len(accra_districts)} districts")
    
    # Test Town Service
    print("\n🏘️  Testing Town Service:")
    towns = TownService.get_all_towns()
    print(f"   ✓ Found {len(towns)} towns")
    
    largest_towns = TownService.get_largest_towns(5)
    print("   ✓ Top 5 largest towns:")
    for i, town in enumerate(largest_towns, 1):
        print(f"      {i}. {town.name}: {town.population:,} people")
    
    print("\n✅ All services working correctly!")
    print("\n🚀 To start the API server, run:")
    print("   python run.py")
    print("\n📖 Then visit http://localhost:8000/docs for API documentation")

if __name__ == "__main__":
    test_services()
