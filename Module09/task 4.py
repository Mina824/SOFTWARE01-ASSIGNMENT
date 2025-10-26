from car import Car
import random

car_list = []
for i in range(10):

    max_speed = random.randint(100, 200)
    car = Car('ABC-' + str(i + 1), max_speed)
    car_list.append(car)

race_distance = 0
race_hours = 0
while race_distance < 10000:
    race_hours += 1
    for car in car_list:
        speed_change = random.randint(-15, 10)
        car.accelerate(speed_change)

        car.drive(1)


        if car.travelled_distance >= 10000:
            race_distance = car.travelled_distance
            break


print(f" Race Finished! Total Duration: {race_hours} hours\n")
print("{:<10} {:<15} {:<12} {:<15} {:<15}".format(
    "Place", "Registration No", "Max Speed", "Current Speed", "Distance (km)"
))
print("-" * 70)


remaining_cars = car_list[:]
place_number = 1

while remaining_cars:

    max_car = remaining_cars[0]
    for car in remaining_cars:
        if car.travelled_distance > max_car.travelled_distance:
            max_car = car


    if place_number == 1:
        place_str = "1st Place"
    elif place_number == 2:
        place_str = "2nd Place"
    elif place_number == 3:
        place_str = "3rd Place"
    else:
        place_str = f"{place_number}th Place"


    print("{:<10} {:<15} {:<12} {:<15} {:<15.1f}".format(
        place_str,
        max_car.registration_number,
        max_car.maximum_speed,
        max_car.current_speed,
        max_car.travelled_distance
    ))

    remaining_cars.remove(max_car)
    place_number += 1
