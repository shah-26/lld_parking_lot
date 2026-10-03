from parking_app.domains.parking_spot import ParkingSpot
from parking_app.domains.parking_spot import SpotType

class ParkingLot:
    def __init__(self):
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot_type: SpotType):
        self.spots.add(ParkingSpot(spot_type))

    def find_available_spot(self):
        for spot in self.spots:
            if spot.is_available():
                return spot

        return None