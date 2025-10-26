import random
from car import Car

class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars
        self.hours_passed = 0

    def hour_passes(self):
        self.hours_passed += 1
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nStatus after {self.hours_passed} hours:")
        print("Reg No    | Max Speed | Current Speed | Distance (km)")
        print("-----------------------------------------------")
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.maximum_speed:<11} {car.current_speed:<15} {car.travelled_distance:.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False



car_list = []


for i in range(10):
    max_speed = random.randint(100, 200)
    car = Car("ABC-" + str(i + 1), max_speed)
    car_list.append(car)

race = Race("Grand Demolition Derby", 8000, car_list)


while not race.race_finished():
    race.hour_passes()
    if race.hours_passed % 10 == 0:
        race.print_status()


print("\n Final results")
race.print_status()
