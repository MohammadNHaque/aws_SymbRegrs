from symreg import Regressor
import random

random.seed(0)

r = Regressor(stagnation_limit=20, verbose=True)
X = [[random.random()-.5, random.random()-.5] for _ in range(100)]
y = [(x[0] + x[1])/2 for x in X]     # We want the average of the arguments

r.fit(X, y)

for score in r.results():
        print(score)
