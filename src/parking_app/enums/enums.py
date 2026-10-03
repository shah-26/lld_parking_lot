from enum import Enum

class TrafficSignal(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

    def can_move(self) -> bool:
        return self in {
            TrafficSignal.GREEN,
            TrafficSignal.YELLOW
            }


class VehicleType(Enum):
    BIKE = "bike"
    CAR = "car"
    COMMERCIAL = "commercial"