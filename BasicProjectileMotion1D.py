import numpy as np
import matplotlib.pyplot as plt

## 1D

y_max = 50 # meters
y_min = 0 # floor

x_value = 5

time = 100

y_values = np.linspace(y_min, y_max, time)
x_value = np.ones(y_values.size)
plt.plot(x_value, y_values)

## 2D

y_max2D = 50 # meters
y_min2D = 0 # floor

x_value_min = 0
x_value_max = 20


y_values2D = np.linspace(y_max2D, y_min2D, time)
x_values2D = np.linspace(x_value_min, x_value_max, time)

plt.plot(x_values2D, y_values2D)




plt.show()




