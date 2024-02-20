import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import arviz as az
import pymc as pm

'''
Executie:
robertantohi@Roberts-MacBook-Pro Marire % poetry run python sol2.py
WARNING (pytensor.tensor.blas): Using NumPy C-API based implementation for BLAS functions.
[12]
3
/Users/robertantohi/Desktop/PMP-2023/Marire/sol2.py:25: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  not_buy=(int)(n-Y)
9
[7.20959491]
/Users/robertantohi/Desktop/PMP-2023/Marire/sol2.py:41: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  not_buy=(int)(n-Y)
Valoare maxima a lui alpha pentru care clientii care nu cumpara sa nu stea mai mult de 15 minute, cu probabilitate de 95%: 9.099999999999985
Valoare medie asteptare: [10.29552729]
'''

#a
buy_prob=0.2
a=5
n=stats.poisson.rvs(20, size=1)
Y=stats.binom.rvs(n,buy_prob)
print(n)
print(Y)
not_buy=(int)(n-Y)
print(not_buy)

time_spent_not_buy=stats.expon.rvs(a, size=1)
print(time_spent_not_buy)
time_spent_buy=stats.expon.rvs(a+1,size=1)

#b
ok=1

while ok==1:
    prob=0
    for i in range(1000):
        maxtime=1
        n=stats.poisson.rvs(20, size=1)
        Y=stats.binom.rvs(n,buy_prob)
        not_buy=(int)(n-Y)
        for j in range(not_buy):
            time_spent_not_buy=stats.expon.rvs(a,size=1)
            if time_spent_not_buy>15:
                maxtime=0
        if maxtime==1:
            prob+=1
    if prob>=950:
        a+=0.1
    else:
        ok=0
        
print("Valoare maxima a lui alpha pentru care clientii care nu cumpara sa nu stea mai mult de 15 minute, cu probabilitate de 95%: "+str(a))
#print(a)

#c
avg=0
for i in range(1000):
    time_spent_not_buy=stats.expon.rvs(a, size=1)
    #print(time_spent_not_buy)
    time_spent_buy=stats.expon.rvs(a+1,size=1)
    total=buy_prob*time_spent_buy+(1-buy_prob)*time_spent_not_buy
    total/=1000
    avg+=total
    
print("Valoare medie asteptare: "+str(avg))
#print(avg)