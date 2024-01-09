import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


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


def metropolis(func, draws=10000):
    """A very simple Metropolis implementation"""
    trace = np.zeros(draws)
    old_x = 0.5 # func.mean()
    old_prob = func.pdf(old_x)
    delta = np.random.normal(0, 0.5, draws)
    for i in range(draws):
        new_x = old_x + delta[i]
    new_prob = func.pdf(new_x)
    acceptance = new_prob / old_prob
    if acceptance >= np.random.random():
        trace[i] = new_x
        old_x = new_x
        old_prob = new_prob
    else:
        trace[i] = old_x
    return trace

beta_params = [(1, 1), (20, 20), (1, 4)]
for (a_prior, b_prior) in beta_params:
    func = stats.beta(a_prior, b_prior)
    trace = metropolis(func=func)
    x = np.linspace(0.01, .99, 100)
    y = func.pdf(x)
    plt.xlim(0, 1)
    plt.plot(x, y, 'C1-', lw=3, label='True distribution')
    plt.hist(trace[trace > 0], bins=25, density=True, label='Estimated distribution')
    plt.xlabel('x')
    plt.ylabel('pdf(x)')
    plt.yticks([])
    plt.legend()
    plt.show()
    data = np.repeat([0, 1], (a_prior, b_prior))
    points = 10
    h = data.sum()
    t = len(data) - h
    grid, posterior = posterior_grid(points, h, t)
    plt.plot(grid, posterior, 'o-')
    plt.title(f'heads = {h}, tails = {t}')
    plt.yticks([])
    plt.xlabel('θ')
    plt.show()