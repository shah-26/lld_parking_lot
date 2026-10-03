
from parking_app.enums.enums import TrafficSignal

def run():
    print("Starting the Parking App...")
    if TrafficSignal.RED.can_move():
        print("You can move.")
    if TrafficSignal.YELLOW.can_move():
        print("You can move.")
    if TrafficSignal.GREEN.can_move():
        print("You can move.")





if __name__ == "__main__":
    run()