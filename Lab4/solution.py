import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import poisson
import arviz as az

#Number of customers
# Create the Poisson probability mass function

rvs = stats.poisson.rvs(mu=20, size=10000)

print(rvs)

az.plot_posterior(rvs)
plt.show()

#Placing order

ord=stats.norm.rvs(2,0.5,size=10000)

print(ord)

az.plot_posterior(ord)
plt.show()

#Pregatire_comanda

a=5
com=stats.expon.rvs(a, size=10000)

print(com)

az.plot_posterior(com)
plt.show()


# Create the plot
