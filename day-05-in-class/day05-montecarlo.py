import random
import math
import matplotlib.pyplot as plt
num_points = []
for i in range(1000):
    num_points.append(i+16)
def monte(num_points):
    count = 0
    for i in range(num_points):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if((x**2 + y**2)**0.5 < 1 and (x**2 + y**2)**0.5 > 0.5):
            count += 1
    area_computed = 4*count/num_points
    area_real = math.pi - (0.5**2)*math.pi
    error = abs((area_computed-area_real)/area_real)
    return(area_computed,area_real,error)

def error_plot(num_points):
    x_vals = []
    y_vals = []
    for i in num_points:
        x_vals.append(i)
        y_vals.append(monte(i)[2])
    return(x_vals,y_vals)
x_vals,y_vals = error_plot(num_points)
plt.plot(x_vals,y_vals)
plt.show()
