
class Elevator :
    def __init__(self, lift_num, min_floor, max_foor, on_floor=0) :
        self.lift_number = lift_num
        self.is_operational = True
        self.max_foor = max_foor
        self.min_floor = min_floor
        self.is_selected = False
        self.is_running = False
        self.on_floor = on_floor
        self.is_moving_up = True
        self.door_open = False
        self.service_list = []
        # self.is_overload = False


    def open_door(self) :
        # print(f"Lift {self.lift_number} door opening..")
        self.door_open = True
        return self.door_open


    def close_door(self) :
        # print(f"Lift {self.lift_number} door closing..")
        self.door_open = False
        return self.door_open


    def current_status(self):
        if self.is_moving_up :
            return self.is_moving_up
        else :
            self.is_moving_up = False
            return self.is_moving_up


    def process_request():
        pass



    def reset_lift_params() :
        pass


