from car import Car

def drive(self, hours):
    self.travelled_distance += self.current_speed * hours
car = Car("ABC-123", 142)


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.drive(1.5)
print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance, "km")