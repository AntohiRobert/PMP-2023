import numpy as np
import matplotlib.pyplot as plt

def approxpi(N = 10000):
    x, y = np.random.uniform(-1, 1, size=(2, N))
    inside = (x**2 + y**2) <= 1
    pi = inside.sum()*4/N
    error = abs((pi - np.pi) / pi) * 100
    outside = np.invert(inside)
    #plt.figure(figsize=(8, 8))
    #plt.plot(x[inside], y[inside], 'b.')
    #plt.plot(x[outside], y[outside], 'r.')
    #plt.plot(0, 0, label=f'π*= {pi:4.3f}\n
    #error = {error:4.3f}', alpha=0)
    #plt.axis('square')
    #plt.xticks([])
    #plt.yticks([])
    #plt.legend(loc=1, frameon=True, framealpha=0.9)
    return error

listn=[100,1000,10000,100000]
errn=[]

for n in listn:
    err=[]
    for i in range(1000):
        err.append(approxpi(10000))
    avg=np.mean(err)
    std=np.std(err)
    errn.append(avg)
    print(str(n)+" "+str(avg)+" "+str(std))
    
'''
rez:
n avg std
100 0.4224829267567249 0.3205077924583043
1000 0.41943201922389467 0.3174294736543791
10000 0.4094103347220888 0.3174572715122629
100000 0.41600368078377375 0.30601387120726825
In concluzie, rata erorii si deviatia standard scad daca n creste.
'''