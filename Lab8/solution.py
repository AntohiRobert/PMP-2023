import pymc as pm
import pandas as pd
import numpy as np
import arviz as az
from matplotlib import pyplot

data = pd.read_csv('Prices.csv')

print(data['Price'])

with pm.Model() as model:
    # a priori slab informativi
    alpha = pm.Normal('alpha', mu=1, sigma=7)
    beta1 = pm.Normal('beta1', mu=1, sigma=8)
    beta2 = pm.Normal('beta2', mu=0.5, sigma=5)
    sigma = pm.HalfNormal('sigma', sigma=2)

    #definim mu
    mu = alpha + beta1 * data['Speed'] + beta2 * np.log(data['HardDrive'])

    #Distributie
    y = pm.Normal('y', mu=mu, sigma=sigma, observed=data['Price'])

    # a posteriori
    trace = pm.sample(2000)


az.summary(trace)
az.plot_posterior(trace)
pyplot.show()

az.plot_posterior(trace.posterior['beta1'])
pyplot.show

beta1_hdi = pm.hdi(trace.posterior['beta1'], hdi_prob=0.95)
beta2_hdi = pm.hdi(trace.posterior['beta2'], hdi_prob=0.95)

print(beta1_hdi)
print(beta2_hdi)
'''
Dimensions:  (hdi: 2)
Coordinates:
  * hdi      (hdi) <U6 'lower' 'higher'
Data variables:
    beta1    (hdi) float64 14.2 15.48
<xarray.Dataset>
Dimensions:  (hdi: 2)
Coordinates:
  * hdi      (hdi) <U6 'lower' 'higher'
Data variables:
    beta2    (hdi) float64 219.2 231.5
'''

#Cum beta1 si beta2 sunt semnificativ diferite de 0(95% hdi), inseamna ca da, frecventa procesorului si marimea HDD-ului
#sunt predictori utili ai pretului de vanzare

print("Pret asteptat pt cumparare calculator")
price = trace.posterior['alpha']+trace.posterior['beta1']*33+trace.posterior['beta2']*np.log(540)

price_hdi = pm.hdi(price, hdi_prob=0.9)

print(price_hdi)


'''
print("Pret vanzare calculator")
with model:
    post_predictive=pm.sample_posterior_predictive(trace)

print(post_predictive.observed_data)


post_predictive_hdi = pm.hdi(post_predictive.observed_data['y'], hdi_prob=0.9)

print("Pret vanzare: ", post_predictive_hdi)

'''

list=[]
for i in range(len(data['Premium'])):
    ok=0
    val=data['Premium'][i]
    if val=="yes":
        ok=1
    list.append(ok)
    #data['Premium'][i].replace(val,ok)
    #print(data['Premium'][i])

data.insert(0,"Premiumbinary", list, True)
print(data['Premiumbinary'])


with pm.Model() as model2:
    # a priori slab informativi
    alpha = pm.Normal('alpha', mu=1, sigma=7)
    beta1 = pm.Normal('beta1', mu=1, sigma=8)
    beta2 = pm.Normal('beta2', mu=0.5, sigma=5)
    beta3 = pm.Normal('beta3', mu=1, sigma=6)
    sigma = pm.HalfNormal('sigma', sigma=2)

    #definim mu
    mu = alpha + beta1 * data['Speed'] + beta2 * np.log(data['HardDrive']) +beta3*data['Premiumbinary']

    #Distributie
    y = pm.Normal('y', mu=mu, sigma=sigma, observed=data['Price'])

    # a posteriori
    trace2 = pm.sample(2000)

az.summary(trace2)
az.plot_posterior(trace2)
pyplot.show()

print("Beta3 hdi:")
beta3_hdi = pm.hdi(trace2.posterior['beta3'], hdi_prob=0.95)
print(beta3_hdi)

'''
Beta3 hdi:
<xarray.Dataset>
Dimensions:  (hdi: 2)
Coordinates:
  * hdi      (hdi) <U6 'lower' 'higher'
Data variables:
    beta3    (hdi) float64 16.03 38.88

Deci, faptul ca producatorul e premium afecteaza pretul, intrucat beta3 95% hdi e semnificativ diferit de 0
'''