import numpy as np
import matplotlib.pyplot as plt

marks = np.random.randint(0, 21, 60)

plt.hist(marks)
plt.title("Marks Distribution")
plt.show()