from parking_app.enums.enums import VehicleType
import uuid
class Vehicle:
    def __init__(self, vehcile_type: VehicleType):
        self.vehicle_id:str = str(uuid.uuid4())
        self.vehicle_type = vehcile_type
