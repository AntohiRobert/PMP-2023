import random

firstplayerwin=0
secondplayerwin=0

random.seed(5)
for i in range(10000):
    J0=0
    J1=0
    r = random.randint(0,1000000)
    #print(r)
    if r%2==0:
        #J0 arunca primul
        t = random.randint(0,1000000)
        #print(t)
        if t%2==0:
            J0=1
            #J0 obtine stema, J1 arunca de 2 ori
            j11=random.randint(0,1000000)
            #print(j11)
            j12=random.randint(0,1000000)
            #print(j12)
            if j11%3!=0:
                J1+=1
            if j12%3!=0:
                J1+=1
        else:
            J0=0
            #J0 nu obtine stema, J1 arunca o data
            j11=random.randint(0,1000000)
            if j11%3!=0:
                J1+=1
        if J0>=J1:
            firstplayerwin+=1
        else:
            secondplayerwin+=1
    else:
        #J1 arunca primul
        t=random.randint(0,1000000)
        if t%3!=0:
            J1=1
            #J1 obtine stema, J0 arunca de 2 ori
            j01=random.randint(0,1000000)
            j02=random.randint(0,1000000)
            if j01%2==0:
                J0+=1
            if j02%2==0:
                J0+=1
        else:
            J1=0
            #J1 nu obtine stema, J0 arunca o data
            j01=random.randint(0,1000000)
            if j01%2==0:
                J0+=1
        if J1>=J0:
            secondplayerwin+=1
        else:
            firstplayerwin+=1

print("First player win " +str(firstplayerwin))
print("Second player win " +str(secondplayerwin))

#First player win 3883
#Second player win 6117

