import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np




L = 5
grid = np.zeros((L, L), dtype=int)

for step in range(20):
    i = random.randrange(L)
    j = random.randrange(L)
    
    grid[i, j] += 1
    if grid[i, j] >= 4:
     grid[i, j] = 0
     

    print(f"step {step}, max height {grid.max()}")

    plt.imshow(grid)
plt.colorbar()
plt.show()
# Simple implementation of a 2D Sandpile Model (SOC)


    
