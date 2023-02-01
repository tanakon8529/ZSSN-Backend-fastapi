from pydantic import BaseModel

class SurvivorModel(BaseModel):
    id: str
    name: str = None
    age: int = None
    gender: str = None
    latitude: float = None
    longitude: float = None
    infected: bool = False
    created_at: str
    updated_at: str

class InventoryModel(BaseModel):
    id: str
    survivor_id: str
    water: int = 0
    food: int = 0
    medication: int = 0
    ammunition: int = 0
    created_at: str
    updated_at: str

class ReportModel(BaseModel):
    id: str
    infected_percentage: float = None
    non_infected_percentage: float = None
    avg_water: float = None
    avg_food: float = None
    avg_medication: float = None
    avg_ammunition: float = None
    points_lost: int = None
    created_at: str
    updated_at: str
