import numpy as np
import matplotlib.pyplot as plt
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

'''
robertantohi@Roberts-MacBook-Pro Marire % poetry run python sol1.py
Probabilitatea ca maine sa ploua: +------------+---------------+
| Ploaie     |   phi(Ploaie) |
+============+===============+
| Ploaie(Da) |        0.4690 |
+------------+---------------+
| Ploaie(Nu) |        0.5310 |
+------------+---------------+
Probabilitatea ca maine sa ploua, avand in vedere ca vremea este innorata: +------------+---------------+
| Ploaie     |   phi(Ploaie) |
+============+===============+
| Ploaie(Da) |        0.4000 |
+------------+---------------+
| Ploaie(Nu) |        0.6000 |
+------------+---------------+
Probabilitatea ca maine sa ploua, avand in vedere ca precizia citirii barometrului este scazuta: +------------+---------------+
| Ploaie     |   phi(Ploaie) |
+============+===============+
| Ploaie(Da) |        0.4158 |
+------------+---------------+
| Ploaie(Nu) |        0.5842 |
+------------+---------------+
Probabilitatea ca astazi sa fie o zi innorata, avand in vedere ca va ploua maine: +-----------------------+----------------------+
| Starea Vremii         |   phi(Starea Vremii) |
+=======================+======================+
| Starea Vremii(Soare)  |               0.5181 |
+-----------------------+----------------------+
| Starea Vremii(Noros)  |               0.4264 |
+-----------------------+----------------------+
| Starea Vremii(Ploios) |               0.0554 |
+-----------------------+----------------------+
'''

#a

model = BayesianNetwork([
    ('Starea Vremii', 'Precizia Citirii Barometrului'),
    ('Starea Vremii', 'Ploaie'),
    ('Precizia Citirii Barometrului', 'Ploaie')
])

#cpd-urile
cpd_stare_vremii = TabularCPD(variable='Starea Vremii', variable_card=3,
                              values=[[0.3], [0.5], [0.2]],
                              state_names={'Starea Vremii': ['Soare', 'Noros', 'Ploios']})

cpd_precizie = TabularCPD(variable='Precizia Citirii Barometrului', variable_card=3, evidence=['Starea Vremii'],
                          evidence_card=[3],
                          values=[[0.7, 0.4, 0.2],  # Mare
                                  [0.2, 0.4, 0.5],  # Medie
                                  [0.1, 0.2, 0.3]], # Scazuta
                          state_names={'Precizia Citirii Barometrului': ['Mare', 'Medie', 'Scazuta'],
                                       'Starea Vremii': ['Soare', 'Noros', 'Ploios']})

cpd_ploaie = TabularCPD(variable='Ploaie', variable_card=2, 
                        evidence=['Starea Vremii', 'Precizia Citirii Barometrului'],
                        evidence_card=[3, 3],
                        values=[[0.8, 0.8, 0.9, 0.4, 0.4, 0.4, 0.1, 0.1, 0.2],  # Da
                                [0.2, 0.2, 0.1, 0.6, 0.6, 0.6, 0.9, 0.9, 0.8]], # Nu
                        state_names={'Ploaie': ['Da', 'Nu'],
                                     'Starea Vremii': ['Soare', 'Noros', 'Ploios'],
                                     'Precizia Citirii Barometrului': ['Mare', 'Medie', 'Scazuta']})


#adaugare si verificare model
model.add_cpds(cpd_stare_vremii, cpd_precizie, cpd_ploaie)
assert model.check_model()

# variable elimination
inference = VariableElimination(model)

# b. Probabilitatea ca maine sa ploua
prob_ploaie = inference.query(variables=['Ploaie'])
print("Probabilitatea ca maine sa ploua:", prob_ploaie)

# c. Probabilitatea ca maine sa ploua, avand in vedere ca vremea este innorata
prob_ploaie_innorat = inference.query(variables=['Ploaie'], evidence={'Starea Vremii': 'Noros'})
print("Probabilitatea ca maine sa ploua, avand in vedere ca vremea este innorata:", prob_ploaie_innorat)

# d. Probabilitatea ca maine sa ploua, avand in vedere ca precizia citirii barometrului este scazuta
prob_ploaie_precizie_scazuta = inference.query(variables=['Ploaie'], evidence={'Precizia Citirii Barometrului': 'Scazuta'})
print("Probabilitatea ca maine sa ploua, avand in vedere ca precizia citirii barometrului este scazuta:", prob_ploaie_precizie_scazuta)

# e. Probabilitatea ca astazi sa fie o zi innorata, avand in vedere ca va ploua maine
prob_innorat_daca_ploaie = inference.query(variables=['Starea Vremii'], evidence={'Ploaie': 'Da'})
print("Probabilitatea ca astazi sa fie o zi innorata, avand in vedere ca va ploua maine:", prob_innorat_daca_ploaie)