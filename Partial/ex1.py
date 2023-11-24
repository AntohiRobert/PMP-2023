import random
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx

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

#Punctul 2

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianNetwork([('First_throw', 'J0_first_round'), ('First_throw', 'J1_first_round'), ('J0_first_round')])

# Defining individual CPDs.
cpd_FT = TabularCPD(variable='First_throw', variable_card=2, values=[[0.5], [0.5]]) #First throw
cpd_J0_first_round = TabularCPD(variable='J0_first_round', variable_card=2, values=[[0.5], [0.5]]) # First player toss in first round
cpd_J1_first_round = TabularCPD(variable='J1_first_round', variable_card=2, values=[[0.66], [0.33]]) # Second player toss in first round

# The CPD for C is defined using the conditional probabilities based on U and R
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.5, 0.2, 0.0], 
                           [0.2, 0.5, 0.8, 1.0]],
                  evidence=['U', 'R'],
                  evidence_card=[2, 2])

# Associating the CPDs with the network
model.add_cpds(cpd_r, cpd_u, cpd_c)

