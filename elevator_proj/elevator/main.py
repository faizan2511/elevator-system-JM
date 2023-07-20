
class Elevator :
    def __init__(self, lift_num, min_floor, max_foor, on_floor=0) :
        self.lift_number = lift_num
        self.is_operational = True
        self.max_foor = max_foor
        self.min_floor = min_floor
        self.is_selected = False
        self.is_running = False
        self.on_floor = on_floor
        self.direction = 1
        # self.is_overload = False
        self.service_list = []

    def open_door(self) :
        print(f"Lift {self.lift_number} door opening..")
        self.door_open = True

    def close_door(self) :
        print(f"Lift {self.lift_number} door closing..")
        self.door_open = True



