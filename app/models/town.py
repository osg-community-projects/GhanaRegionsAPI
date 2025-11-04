from pydantic import BaseModel
from typing import Optional

class TownBase(BaseModel):
    name: str
    district_id: int
    population: Optional[int] = None

class Town(TownBase):
    id: int
    
    class Config:
        from_attributes = True

class TownCreate(TownBase):
    pass

class TownUpdate(BaseModel):
    name: Optional[str] = None
    district_id: Optional[int] = None
    population: Optional[int] = None
