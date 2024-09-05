from random import uniform
import matplotlib.pyplot as plt

square = 10 * 10
circle_radius = 5

rand_points_x = []
rand_points_y = []
colors = []

total_points = 10000
in_circle_points = 0

for _ in range(total_points):
    rand_points_x.append(uniform(-5, 5))
    rand_points_y.append(uniform(-5, 5))


for i in range(total_points):
    hip = ((rand_points_x[i] ** 2) + (rand_points_y[i] ** 2)) ** (1 / 2)
    if hip <= circle_radius:
        in_circle_points += 1
        colors.append("blue")

    else:
        colors.append("green")

pi = (in_circle_points / total_points) * 4

plt.scatter(rand_points_x, rand_points_y, c=colors)
plt.title(f"PI: {pi}")
plt.show()
