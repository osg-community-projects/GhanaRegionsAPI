from pydantic import BaseModel
from typing import List, Optional

class RegionBase(BaseModel):
    name: str
    capital: str

class Region(RegionBase):
    id: int
    
    class Config:
        from_attributes = True

class RegionWithDistricts(Region):
    districts: List["District"] = []

class RegionCreate(RegionBase):
    pass

class RegionUpdate(BaseModel):
    name: Optional[str] = None
    capital: Optional[str] = None
