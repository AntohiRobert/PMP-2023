import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az

np.random.seed(1)

#x = stats.norm.rvs(0, 1, size=10000) # Distributie normala cu media 0 si deviatie standard 1, 1000 samples
#y = stats.uniform.rvs(-1, 2, size=10000) # Distributie uniforma intre -1 si 1, 1000 samples . Primul parametru fiind limita inferioara a intervalului, al doilea parametru fiind "marimea" intervalului, aka [-1,-1+2] = [-1,1] 
#z = x+y # Compunerea prin insumare a celor 2 distributii

#az.plot_posterior({'x':x,'y':y,'z':z}) # Afisarea aproximarii densitatii probabilitatilor, mediei, intervalului etc. variabilelor x,y,z
#plt.show()

#x= stats.expon.rvs(scale=1/4, size=10000)
#y= stats.expon.rvs(scale=1/6, size=10000)
#z=0.4*x+0.6*y

#az.plot_posterior({'x':x,'y':y,'z':z}) # Afisarea aproximarii densitatii probabilitatilor, mediei, intervalului etc. variabilelor x,y,z
#plt.show()

x=stats.gamma.rvs(4,scale=1/3,size=10000)
y=stats.gamma.rvs(4,scale=1/2,size=10000)
z=stats.gamma.rvs(5,scale=1/2,size=10000)
t=stats.gamma.rvs(5,scale=1/3,size=10000)

latency=stats.expon.rvs(scale=1/4, size=10000)

time=0.25*x+0.25*y+0.3*z+0.2*t+latency

az.plot_posterior({'time':time})
plt.show()