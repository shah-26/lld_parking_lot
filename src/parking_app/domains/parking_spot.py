from enum import Enum
import uuid

class SpotType(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class ParkingSpot:
    def __init__(self, spot_type: SpotType):
        self.spot_id:str = str(uuid.uuid4())
        self.spot_type = spot_type
        self.vehicle_id:str = None

    def is_available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle_id:str):
        if not self.is_available():
            raise Exception("Spot is occupied!")
        self.vehicle_id = vehicle_id

    def unpark_vehicle(self) -> str:
        if self.is_available():
            self.vehicle_id = None
