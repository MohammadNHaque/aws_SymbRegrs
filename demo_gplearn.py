# create some synthetic data 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



nsample = 400
sig     = 0.2

x = np.linspace(-50, 50, nsample)
X = np.column_stack((x/5, 10*np.sin(x), (x-5)**3, np.ones(nsample)))
beta = [0.01, 1, 0.001, 5.]

y_true = np.dot(X, beta)
y = y_true + sig * np.random.normal(size=nsample)

df     = pd.DataFrame()
df['x']=x
df['y']=y



# GPlearn imports and implementation
from gplearn.genetic import SymbolicRegressor
from sympy import *

#we split our dataset in train/test:
X = df[['x']]
y = df['y']
y_true = y
X_train, X_test, y_train, y_test = train_test_split(X, y, 
         test_size=0.30, random_state=42)

# First Test
function_set = ['add', 'sub', 'mul', 'div','cos','sin','neg','inv']
est_gp = SymbolicRegressor(population_size=5000,function_set=function_set,
                                    generations=40, stopping_criteria=0.01,
                                    p_crossover=0.7, p_subtree_mutation=0.1,
                                    p_hoist_mutation=0.05, p_point_mutation=0.1,
                                    max_samples=0.9, verbose=1,
                                    parsimony_coefficient=0.01, random_state=0,
                                    feature_names=X_train.columns)

#We define a dictionary called converter: its use will be clear later but essentially we need it to convert a function name, or string, in its equivalent python mathematical code.
converter = { 'sub': lambda x, y : x - y,
              'div': lambda x, y : x/y,
              'mul': lambda x, y : x*y,
              'add': lambda x, y : x + y,
              'neg': lambda x    : -x,
              'pow': lambda x, y : x**y,
              'sin': lambda x    : sin(x),
              'cos': lambda x    : cos(x),
              'inv': lambda x: 1/x,
              'sqrt': lambda x: x**0.5,
              'pow3': lambda x: x**3
            }

#We then fit the data, we evaluate our R2 score and with the help of simpyfy we print the resulting expression:
est_gp.fit(X_train, y_train)
print('R2:',est_gp.score(X_test,y_test))
next_e = sympify((est_gp._program), locals=converter)
#next_e

#Calculate the score of Gplearn
y_gp = est_gp.predict(X_test)
score_gp = est_gp.score(X_test, y_test)
print(f"Gplearn: {score_gp}")


##improve gplearn by adding new function
#from gplearn.functions import make_function
#
#def pow_3(x1):
#    f = x1**3
#    return f
#
#pow_3 = make_function(function=pow_3,name='pow3',arity=1) # add the new function to the function_set
#function_set = ['add', 'sub', 'mul', 'div','cos','sin','neg','inv',pow_3]
#
#est_gp = SymbolicRegressor(population_size=5000,function_set=function_set,
#        generations=45, stopping_criteria=0.01,
#        p_crossover=0.7, p_subtree_mutation=0.1,
#        p_hoist_mutation=0.05, p_point_mutation=0.1,
#        max_samples=0.9, verbose=1,
#        parsimony_coefficient=0.01, random_state=0,
#        feature_names=X_train.columns)
#                                                                                                
#
#est_gp.fit(X_train, y_train)
#print('R2:',est_gp.score(X_test,y_test))
#next_e = sympify((est_gp._program), locals=converter)                                                                   
#next_e
#
