import arviz as az
import pandas as pd
from matplotlib import pyplot
import pymc as pm
import statistics
import numpy as np
#import tensorflow as tf

#returns = pd.read_csv(
#    pm.get_data("trafic.csv"), parse_dates=True, index_col=0, usecols=["minut", "nr_masini"]
#)

data=pd.read_csv("auto-mpg.csv")

for x in data.index:
    if data.loc[x,"horsepower"] == "?":
        data.drop(x,inplace=True)

mpg=data.iloc[:, 0]

cp=data.iloc[:, 3]

cp=pd.to_numeric(cp,downcast="float")

print(mpg)

print(cp)

pyplot.scatter(cp,mpg)
pyplot.show()

#mpg_tensor=tf.convert_to_tensor(mpg)
#cp_tensor=tf.convert_to_tensor(cp)

with pm.Model() as model:  # model specifications in PyMC are wrapped in a with-statement
    # Define priors
    sigma = pm.HalfCauchy("sigma", beta=10)
    intercept = pm.Normal("Intercept", 0, sigma=20)
    slope = pm.Normal("slope", 0, sigma=20)

    #print(type(intercept))
    #print(type(slope))
    #print(type(cp_tensor))
    #muIn = intercept+slope*cp

    # Define likelihood
    likelihood = pm.Normal("y", mu=intercept+slope*cp, sigma=sigma, observed=mpg)

    # Inference!
    # draw 3000 posterior samples using NUTS sampling
    idata = pm.sample(3000)

#best_regression_line = idata.intercep

print(idata.posterior)

az.plot_trace(idata, figsize=(10, 7))
pyplot.show()

intercept_mean = np.mean(idata.posterior["Intercept"]).item()

slope_mean = np.mean(idata.posterior["slope"]).item()

print(intercept_mean)
print(slope_mean)

best_regression_line = intercept_mean +slope_mean*cp
#Cu cat cp e mai mare, cu atat mpg e mai mare. cp si mpg sunt invers corelate

print(mpg)

print(cp)

print(data)