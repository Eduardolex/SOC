import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

L = 64
THRESH = 4
grid = np.zeros((L, L), dtype=int)
rng = random.Random()

def drive():
    i = rng.randrange(L)
    j = rng.randrange(L)
    grid[i, j] += 1
    return (i, j)

def relax():
    q = deque(np.argwhere(grid >= THRESH))
    topplings = 0

    while q:
        x, y = q.popleft()
        if grid[x, y] < THRESH:
            continue

        grid[x, y] -= THRESH
        topplings += 1

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < L and 0 <= ny < L:
                grid[nx, ny] += 1
                if grid[nx, ny] >= THRESH:
                    q.append((nx, ny))
    return topplings            
print(grid)
plt.imshow(grid)
plt.colorbar()
plt.show()
# Simple implementation of a 2D Sandpile Model (SOC)


    
