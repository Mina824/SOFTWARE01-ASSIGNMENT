
import random
points = int(input("How many points to generate?"))
inside_circle = 0
for _ in range(points):
    x = random.random(-1, 1)
    y = random.random(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

approximate_pi = 4 * inside_circle / points
print("approximate_pi", approximate_pi)
