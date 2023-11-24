import random
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az

import pandas as pd
import pymc as pm

#Partea 1
miu=2.0
sigma=0.5

timp_asteptare=stats.norm.rvs(miu,sigma, size=100)

"""
[1.72629146 1.74480858 1.81805804 1.83825754 1.72372639 2.51194107
 1.83144713 2.3461195  2.00382861 2.85655935 2.12322678 2.02207091
 2.20316586 2.15781207 2.4584968  1.92649981 1.42038333 2.71406112
 2.3913622  1.70478878 2.67377941 1.39702482 2.01760647 1.73157326
 1.59164473 2.23924147 2.94577378 2.76011902 1.70109123 1.60305541
 1.98652382 2.64306565 1.53991296 2.335324   1.95037368 2.32510071
 1.99137024 2.27690222 2.15483127 2.08238812 2.04744326 2.04168816
 2.28601014 1.97354081 1.77526613 1.7759947  0.92774837 2.85662336
 2.46977398 1.97211778 1.26657888 2.46251854 1.97789798 2.49484654
 1.53224744 1.52074334 2.96718899 2.84293184 1.82562064 2.30151578
 1.29263456 1.4678803  1.30748307 0.56448196 1.5732856  2.00986076
 2.4933609  2.44117722 2.06916161 2.5195432  2.27641021 1.93630996
 1.29530586 1.6851742  3.21183362 2.29954111 2.08592204 1.2180511
 2.46623369 1.42134226 1.51981057 2.02334497 2.11997064 2.93743633
 1.94361064 2.73889576 2.80757385 2.24247851 2.29376916 1.44475959
 1.30743768 1.0700427  1.97201129 2.70280654 1.95090396 2.31232517
 1.62973309 1.71929242 1.92776196 1.47916892]

"""

print(timp_asteptare)

#Partea 2
model = pm.Model()

with model:
    basic_model = pm.Model()


#Sursa: https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/pymc_overview.html

with basic_model:
    # Priors for unknown model parameters
    #Distributia Poisson e adesea folosita pt un nr de evenimente independente intr-un anumit interval orar
    mu=pm.Poisson("mu", mu=2)
    #Nr de minute per client
    #mu=60/mu
    #Half normal e adesea folosit pt sigma
    sigma = pm.HalfNormal("sigma", sigma=0.3)

    # Expected value of outcome
    #timp_asteptare=stats.norm.rvs(miu,sigma, size=100)

    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=timp_asteptare)

with basic_model:
    # draw 1000 posterior samples
    idata = pm.sample()

#Partea 3
#Corespunde asteptarilor
print(az.summary(idata))
az.plot_posterior(idata)
plt.show()
"""
        mean     sd  hdi_3%  hdi_97%  mcse_mean  mcse_sd  ess_bulk  ess_tail  r_hat
mu     2.000  0.000   2.000    2.000      0.000    0.000    4000.0    4000.0    NaN
sigma  0.464  0.032   0.404    0.524      0.001    0.001    1738.0    2570.0    1.0
"""