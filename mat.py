import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints,  'o--y')

plt.title('Hello there', loc ='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


plt.grid()

plt.show()