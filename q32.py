import numpy as np

A = np.array([[2, 3, 1],
              [1, -1, 2],
              [3, 4, 1]])

B = np.array([13, 7, 22])

solution = np.linalg.solve(A, B)
print("Solution:", solution)

# Check correctness
check = np.dot(A, solution)
print("Verification:", check)