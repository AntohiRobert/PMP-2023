import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Admission.csv')

print(data.head())

with pm.Model() as model:
    b0 = pm.Normal('b0', mu=0, sigma=20)
    b1 = pm.Normal('b1', mu=0, sigma=20)
    b2 = pm.Normal('b2', mu=0, sigma=20)
    
    #sigmoid
    mu = pm.math.invlogit(b0 + b1 * data['GRE'] + b2 * data['GPA'])

    #Distributie
    y = pm.Normal('y', mu=mu, sigma=20, observed=data['Admission'])
    
    #a posteriori
    trace = pm.sample(2000,target_accept=.95)

print(trace.posterior)

b0_posterior = trace.posterior['b0']
b1_posterior = trace.posterior['b1']
b2_posterior = trace.posterior['b2']

b0_posterior_avg = np.mean(b0_posterior)
b1_posterior_avg = np.mean(b1_posterior)
b2_posterior_avg = np.mean(b2_posterior)

decision_boundary = -b0_posterior_avg / b2_posterior_avg

# Calculul intervalului HDI pentru granița de decizie
hdi = pm.stats.hdi(-b0_posterior / b2_posterior, hdi_prob=0.94)
low_value = hdi['x'].sel(hdi='lower').values
high_value = hdi['x'].sel(hdi='higher').values
print(hdi)
print(low_value)

plt.figure(figsize=(8, 6))

# decision boundary
plt.scatter(data['GRE'], data['GPA'], c=data['Admission'], cmap='coolwarm', alpha=0.7)
plt.colorbar(label='Admission')
plt.xlabel('GRE Score')
plt.ylabel('GPA')

# Linie decizie
plt.axline((decision_boundary, 0), slope=-b1_posterior_avg / b2_posterior_avg, color='black', label='Decision Boundary')

# Zonă HDI 94%
plt.fill_betweenx(np.linspace(data['GPA'].min(), data['GPA'].max(), 100), low_value, high_value, color='gray', alpha=0.3, label='94% HDI')

plt.legend()
plt.title('Decision Boundary si HDI')
plt.show()

student_GRE = 550
student_GPA = 3.5
x = -(b0_posterior_avg + b1_posterior_avg * student_GRE + b2_posterior_avg * student_GPA)
x = np.clip(x, -750, 500)  # Limit the range of x to prevent overflow
student_probability = 1 / (1 + np.exp(x))
#student_probability =  1 / (1 + np.exp(-(b0_posterior_avg + b1_posterior_avg * student_GRE + b2_posterior_avg * student_GPA)))
#student_probability = pm.math.invlogit(b0 + b1 * student_GRE + b2 * student_GPA)

x = -(b0_posterior + b1_posterior * student_GRE + b2_posterior * student_GPA)
x = np.clip(x, -750, 500)  # Limit the range of x to prevent overflow
prob_samples = 1 / (1 + np.exp(x))
#prob_samples = 1 / (1 + np.exp(-(b0_posterior + b1_posterior * student_GRE + b2_posterior  * student_GPA)))
#prob_samples = pm.math.invlogit(b0_posterior + b1_posterior * student_GRE + b2_posterior * student_GPA)
hdi_student_probability = pm.stats.hdi(prob_samples, hdi_prob=0.9)

print("Admission probability:")
print(student_probability)
print("Hdi admission probability:")
print(hdi_student_probability)

student_GRE = 500
student_GPA = 3.2
x = -(b0_posterior_avg + b1_posterior_avg * student_GRE + b2_posterior_avg * student_GPA)
x = np.clip(x, -750, 500)  # Limit the range of x to prevent overflow
student_probability = 1 / (1 + np.exp(x))
#student_probability =  1 / (1 + np.exp(-(b0_posterior_avg + b1_posterior_avg * student_GRE + b2_posterior_avg * student_GPA)))
#student_probability = pm.math.invlogit(b0 + b1 * student_GRE + b2 * student_GPA)

x = -(b0_posterior + b1_posterior * student_GRE + b2_posterior * student_GPA)
x = np.clip(x, -750, 500)  # Limit the range of x to prevent overflow
prob_samples = 1 / (1 + np.exp(x))
#prob_samples = 1 / (1 + np.exp(-(b0_posterior + b1_posterior * student_GRE + b2_posterior  * student_GPA)))
#prob_samples = pm.math.invlogit(b0_posterior + b1_posterior * student_GRE + b2_posterior * student_GPA)
hdi_student_probability = pm.stats.hdi(prob_samples, hdi_prob=0.9)

print("Admission probability second case:")
print(student_probability)
print("Hdi admission probability second case:")
print(hdi_student_probability)