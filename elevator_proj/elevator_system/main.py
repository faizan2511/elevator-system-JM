from elevator.main import Elevator

class ElevatorSystem :
    def __init__(self, num_of_lifts, min_floor, max_floor, request_each, lift_positions=[]) :
        self.number_of_lifts = num_of_lifts
        self.max_floor = max_floor
        self.min_floor = min_floor
        self.elevators = []
        self.request_queue = request_each

        if len(lift_positions) == 0 :
            lift_positions = [0] * num_of_lifts

        # create an array of elevator objects
        for lift_num in range(0, num_of_lifts) :
            new_elevator = Elevator(lift_num, min_floor, max_floor)
            self.elevators.append(new_elevator)
