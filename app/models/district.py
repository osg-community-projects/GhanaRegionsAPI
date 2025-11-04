from pydantic import BaseModel
from typing import List, Optional

class DistrictBase(BaseModel):
    name: str
    region_id: int

class District(DistrictBase):
    id: int
    
    class Config:
        from_attributes = True

class DistrictWithTowns(District):
    towns: List["Town"] = []

class DistrictCreate(DistrictBase):
    pass

class DistrictUpdate(BaseModel):
    name: Optional[str] = None
    region_id: Optional[int] = None
