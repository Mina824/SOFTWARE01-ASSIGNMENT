from car import Car

def accelerate(self, speed_change):
    self.current_speed += speed_change
    if self.current_speed > self.maximum_speed:
        self.current_speed = self.maximum_speed
    elif self.current_speed < 0:
        self.current_speed = 0

Car.accelerate = accelerate

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Final speed after braking: {car.current_speed} km/h")





