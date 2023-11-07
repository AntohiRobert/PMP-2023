import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import pandas as pd

#returns = pd.read_csv(
#    pm.get_data("trafic.csv"), parse_dates=True, index_col=0, usecols=["minut", "nr_masini"]
#)

data=pd.read_csv("trafic.csv")

print(data)

print(data['minut'].describe())
print(data['nr. masini'].describe())

cars4to7=0
cars7to8=0
cars8to16=0
cars16to19=0
cars19to24=0

for i in range(len(data)):
    minut=data.iloc[i]['minut']
    nrmasini=data.iloc[i]['nr. masini']
    if minut<180:
        cars4to7+=nrmasini
    elif minut<240:
        cars7to8+=nrmasini
    elif minut<720:
        cars8to16+=nrmasini
    elif minut<900:
        cars16to19+=nrmasini
    else:
        cars19to24+=nrmasini

print(cars4to7)
print(cars7to8)
print(cars8to16)
print(cars16to19)
print(cars19to24)

#print(data)

#len(returns)

model = pm.Model()


with model:
    prior4to7 = pm.Uniform('prior4to7', 700, 20)
    int4to7_obs = pm.Poisson('obs4to7', mu=prior4to7, observed=cars4to7)
    int7to8 = pm.Poisson(y2)
    int8to16 = pm.Poisson(y3)
    int16to19 = pm.Poisson(y4)
    int19to24 = pm.Poisson(y5)

with model:
    trace = pm.sample(20000)