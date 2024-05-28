import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

num_points = 1000
min_value=0
max_value=1000
grid_size = 200  
colors=np.random.rand(max_value//grid_size,max_value//grid_size,3)
x_coords = np.random.randint(min_value, max_value+1, num_points)
y_coords = np.random.randint(min_value, max_value+1, num_points)

df = pd.DataFrame({
    'X': x_coords,
    'Y': y_coords
})

df.to_excel('coordinates.xlsx', index=False)

def plot_grid():
    fig, ax = plt.subplots()

    for i in range(min_value, max_value, grid_size):
        for j in range(min_value, max_value, grid_size):
            mask = (x_coords >= i) & (x_coords < i + grid_size) & (y_coords >= j) & (y_coords < j + grid_size)
            points_in_grid = df[mask]
            if not points_in_grid.empty:
                ax.scatter(points_in_grid['X'], points_in_grid['Y'], c=colors[i//grid_size][j//grid_size], label=f'Grid {i//grid_size}, {j//grid_size}')

    ax.set_xlabel('X Koordinatları')
    ax.set_ylabel('Y Koordinatları')
    ax.set_title(f'Rastgele Noktaların Görselleştirilmesi (Grid Size: {grid_size}x{grid_size})')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True) 
    plt.show()

plot_grid()
