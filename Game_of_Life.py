import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

''' 
N - size of field
ON - OFF - states of cells
ON = 1 OFF = 0 (255, 0) - colors of cells
'''
N = 50
ON = 255
OFF = 0
vals = [ON, OFF]

# Fill the grid with random values
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

# Main function
def update(data):
    global grid
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
            grid[(i-1)%N, j] + grid[(i+1)%N, j] +
            grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
            grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255

    
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    grid = newGrid
    mat.set_data(grid)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
plt.show()