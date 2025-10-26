from car import Car

def drive(self, hours):
    self.travelled_distance += self.current_speed * hours

Car.drive = drive

car = Car("ABC-123", 142)
car.accelerate(60)
car.drive(1.5)

print(f"Travelled distance: {car.travelled_distance} km")