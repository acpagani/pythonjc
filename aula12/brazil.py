from random import uniform
import matplotlib.pyplot as plt
from math import sin, cos, radians

square = 20 * 20
circle_radius = 5

rand_points_x = []
rand_points_y = []

xl = []
yl = []

xc = []
yc = []
colors = ["green", "yellow", "blue"]

total_points = 10000
in_circle_points = 0

for _ in range(total_points):
    rand_points_x.append(uniform(-20, 20))
    rand_points_y.append(uniform(-20, 20))


for i in range(total_points):
    hip = ((rand_points_x[i] ** 2) + (rand_points_y[i] ** 2)) ** (1 / 2)
    if hip <= circle_radius:
        xc.append(rand_points_x[i])
        yc.append(rand_points_y[i])

    elif -10 <= rand_points_x[i] <= 10 and -10 <= rand_points_y[i] <= 10:
        xl.append(rand_points_x[i] * cos(radians(45)) + rand_points_y[i] * sin(radians(45)))
        yl.append(-rand_points_x[i] * sin(radians(45)) + rand_points_y[i] * cos(radians(45)))

plt.scatter(rand_points_x, rand_points_y, c=colors[0])
plt.scatter(xl, yl, c=colors[1])
plt.scatter(xc, yc, c=colors[2])

plt.show()
