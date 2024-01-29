import pandas as pd
import pymc as pm
import arviz as az
import numpy as np
import math



#Supbct a
data = pd.read_csv('Titanic.csv')
print(data.head())

'''old attempt
for x in data.index:
    if data.loc[x,"Survived"] == "" or data.loc[x,"Pclass"]=="" or data.loc[x,"Age"]=="":
        print(data.loc[x])
        data.drop(x,inplace=True)
'''
        
for x in data.index:
    if data.loc[x,"Survived"] not in {0,1} or data.loc[x,"Pclass"] not in {1,2,3} or not 0< data.loc[x,"Age"]<100:
        print(data.loc[x])
        data.drop(x,inplace=True)
        
#print(data)

#Subpct b
pclass = data["Pclass"].values
age = data["Age"].values
survived = data["Survived"].values
with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sigma=5)
    coef_pclass = pm.Normal('coef_pclass', mu=0, sigma=2)
    coef_age = pm.Normal('coef_age', mu=0, sigma=1)
    
    determ=pm.Deterministic('determ', pm.math.sigmoid(alpha+coef_age*age+coef_pclass*pclass))
    #determ=pm.Deterministic('determ', alpha+coef_age*age+coef_pclass*pclass)
    
    inf=pm.Bernoulli('inf', p=determ, observed=survived)
    
    trace=pm.sample(2000)

'''
Executie:
Auto-assigning NUTS sampler...
Initializing NUTS using jitter+adapt_diag...
Multiprocess sampling (4 chains in 4 jobs)
NUTS: [alpha, coef_pclass, coef_age]
Sampling 4 chains for 1_000 tune and 2_000 draw iterations (4_000 + 8_000 draws total) took 3 seconds.gences]
'''

#Subpct c
age_pasager=30
pclass_pasager=2

alpha_samples = trace.posterior['alpha'].values.flatten()
coef_age = trace.posterior['coef_age'].values.flatten()
coef_pclass = trace.posterior['coef_pclass'].values.flatten()

#Vedem care coeficient are magnitudinea mai mare, si deci influenta mai mare
coef_age_abs_mean=np.mean(abs(coef_age))
coef_pclass_abs_mean=np.mean(abs(coef_pclass))

print(coef_age_abs_mean)
print(coef_pclass_abs_mean)
'''Rezultat:
0.01219706873408851
0.38653965202504015
Observam ca valorile la coef_age sunt mult mai mici decat la coef_pclass, deci probabil
pclass influenteaza mai mult probabilitatea de supravietuire
'''
# Subpct d
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

val_pasager= alpha_samples+coef_age*age_pasager+coef_pclass*pclass_pasager

print(val_pasager)

prob_suprav=[]

for val in val_pasager:
    v=sigmoid(val)
    prob_suprav.append(v)

print(prob_suprav)

medie_probabilitate_suprav = np.mean(prob_suprav)
hdi_probabilitate_suprav = az.hdi(prob_suprav, hdi_prob=0.9)

