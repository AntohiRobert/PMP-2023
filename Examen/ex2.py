import numpy as np
import matplotlib as plt
from scipy import stats


def approx(N):
    x_greater_than_y_squared=0

    for i in range(N):
        x=stats.geom.rvs(0.3)
        y=stats.geom.rvs(0.5)
        if x>y*y:
            x_greater_than_y_squared+=1   
    #print(str(x_greater_than_y_squared)+" out of "+str(N))
    #print("Subpct a Done!")
    p=x_greater_than_y_squared/N
    return p

#print(approx(N))
N=10000
k=30

approx(N)
'''
Output:
4191 out of 10000
Subpct a Done!
'''

vals=[]
for i in range(k):
    p=approx(N)
    vals.append(p)
    
avg=np.mean(vals)
sd=np.std(vals)
print("Average is "+str(avg))
print("Sd is "+str(sd))

'''
Output:
Average is 0.4163766666666667
Sd is 0.00454794336913828
'''