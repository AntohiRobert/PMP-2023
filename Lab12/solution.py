import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#Subpct 1

def posterior_grid(grid_points=50, heads=6, tails=9):
    """
    A grid implementation for the coin-flipping problem
    """
    grid = np.linspace(0, 1, grid_points)
    #prior = np.repeat(1/grid_points, grid_points) # uniform prior
    prior = (grid<= 0.5).astype(int)
    likelihood = stats.binom.pmf(heads, heads+tails, grid)
    posterior = likelihood * prior
    posterior /= posterior.sum()
    return grid, posterior

#data = np.repeat([0, 1], (10, 3))
data = np.repeat([0, 1], (100, 40))
points = 10
h = data.sum()
t = len(data) - h
grid, posterior = posterior_grid(points, h, t)
plt.plot(grid, posterior, 'o-')
plt.title(f'heads = {h}, tails = {t}')
plt.yticks([])
plt.xlabel('θ')
plt.show()