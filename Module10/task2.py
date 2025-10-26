from elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number!")
            return
        print(f"\nRunning elevator {elevator_number} to floor {floor}:")
        self.elevators[elevator_number - 1].go_to_floor(floor)




building = Building(1, 10, 3)
building.run_elevator(1, 7)
building.run_elevator(2, 3)
building.run_elevator(3, 10)
