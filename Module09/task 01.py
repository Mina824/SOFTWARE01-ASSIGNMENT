class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0



car = Car("ABC-123",142)

print(f"Registration number: {car.registration_number}")
print(f"Maximum speed: {car.maximum_speed} ")
print(f"Current speed: {car.current_speed} ")
print(f"Travelled distance: {car.travelled_distance} km")