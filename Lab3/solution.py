from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianNetwork([('I', 'A'), ('C', 'A'), ('C', 'I')])

# Defining individual CPDs.
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.95], [0.05]]) # R=0 fara cutremur, R=1 cutremur

cpd_I = TabularCPD(variable='I', variable_card=2,
                   values=[[[0.01], [0.99]], #C=0
                            [[0.03],[0.97]]], #C=1
                   evidence=['C'],
                   evidence_card=1) # I=0
##?? model cpd cu atatea dependinte nu stiu
# The CPD for A is defined using the conditional probabilities based on I and C
cpd_A = TabularCPD(variable='A', variable_card=2, 
                   values=[[0.8, 0.2, 0.5, 0.95], 
                           [0.2, 0.8, 0.5, 0.05]],
                  evidence=['C', 'I'],
                  evidence_card=[2, 2])

# Associating the CPDs with the network
model.add_cpds(cpd_C, cpd_I, cpd_A)

# Verifying the model
assert model.check_model()

# Performing exact inference using Variable Elimination

#2 infer = VariableElimination(model)
#result = infer.query(variables=['C'], evidence={'A': 1})
#print(result)

#3 infer = VariableElimination(model)
#result = infer.query(variables=['I'], evidence={'A': 0})
#print(result)

#pos = nx.circular_layout(model)
#nx.draw(model, pos=pos, with_labels=True, node_size=4000, font_weight='bold', node_color='skyblue')
#plt.show()