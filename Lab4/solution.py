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

a=4
com=stats.expon.rvs(scale=a, size=10000)

print(com)

az.plot_posterior(com)
plt.show()

#Subpct2:

total=ord+com

print(total)
az.plot_posterior(total)
plt.show()

#Luat din BMH:
print(np.mean(total<15))

a=3
ok=True
while ok:
    a+=0.1
    com=stats.expon.rvs(scale=a, size=10000)
    total=ord+com
    if np.mean(total<15)<0.95:
        ok=False
    if not ok:
        a-=0.1
print(a)
# Create the plot
