import numpy as np
import scipy.stats as stats
import pymc as pm
import matplotlib.pyplot as plt
import arviz as az

#trials = 4
#theta_real = 0.35 # unknown value in a real experiment
#data = stats.bernoulli.rvs(p=theta_real, size=trials)

#data=[0,5,10]

for i in [0.2,0.5]:
    for j in [0,5,10]:
        with pm.Model() as our_first_model:
        # a priori
            #θ = pm.Beta('θ', alpha=1., beta=1.)
            n = pm.Poisson('n', 10)
            buy_probability = i
            obs=j
            Y = pm.Binomial("obs", n, buy_probability, observed=obs)
        # likelihood
            Infered_n = pm.sample()
            #y = pm.Bernoulli('y', p=θ, observed=data)
            #idata = pm.sample(1000, random_seed=123, return_inferencedata=True)
        print("Probability="+str(i)+", Observed="+str(j) )
        print(az.summary(Infered_n, kind="stats"))
        az.plot_posterior(Infered_n)
        
        
plt.show()
