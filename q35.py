import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = x**2 + 2*x
z = np.sin(y)

plt.plot(x, y, label="y = x^2 + 2x")
plt.plot(x, z, label="z = sin(y)")

plt.legend()
plt.show()