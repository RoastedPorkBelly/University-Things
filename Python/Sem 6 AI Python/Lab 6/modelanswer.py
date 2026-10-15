
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from math import inf, fabs
import pandas as pd
import sys
import numpy as np
from sklearn.metrics import mean_squared_error

# dataset
diabetes = datasets.load_diabetes()
x = diabetes.data[:,2]
y = diabetes.target

# parameter definition
learningrate = 0.3
m = []
c = []
J = []

# initialise m and c
def initialiseMFromData(x,y):
  dt = pd.DataFrame({"x": x, "y": y})
  xmin = dt.x.min()
  xmax = dt.x.max()
  ymin = dt[dt.x == xmin].y.min()
  ymax = dt[dt.x == xmax].y.max()
  return (ymax - ymin) / (xmax - xmin)

def initialiseCFromData(x,y):
  dt = pd.DataFrame({"x": x, "y": y})
  return dt[dt.x == dt.x.abs().min()].y.mean()

# m.append(initialiseMFromData(x,y))
m.append(0)
# c.append(initialiseCFromData(x,y))
c.append(0)

print(f"Initial values:\n  m {m[0]}\n  c {c[0]}")

# termination condition
J_min = 0.001
del_J_min = 0.00001 # proportion of J
max_iter = 10000

# linear regression model
def model(x, param):
  return param['m'] * x + param['c']

# calculate least-squares cost
def cost(x, y, param):
  dt = pd.DataFrame({"x": x, "y": y})
  dt['y_pred'] = dt.x.apply(lambda x: model(x,param))
  dt['sqrd_error'] = (dt.y - dt.y_pred)**2
  return dt.sqrd_error.mean()

# calculate derivative wrt each parameter
def derivatives(x,y,param):
  dt = pd.DataFrame({"x": x, "y": y})
  dcostdm = dt.x * (dt.y - param['m'] * dt.x - param['c'])
  dcostdm = dcostdm.mean() * -2
  dcostdc = dt.y - param['m'] * dt.x - param['c']
  dcostdc = dcostdc.mean() * -2
  return {'m': dcostdm, 'c': dcostdc}

# calculate change in J
def get_del_J():
  if len(J) > 1:
    return fabs(J[-1] - J[-2])/J[-1]
  else:
    return inf

plt.scatter(x,y,color="red")
plt.ion()
plt.show()
line = None
J.append(cost(x, y, {"m": m[-1], "c": c[-1]}))
while J[-1] > J_min and get_del_J() > del_J_min and len(J) < max_iter:
  der = derivatives(x, y, {"m": m[-1], "c": c[-1]})
  m.append(m[-1] - learningrate * der['m'])
  c.append(c[-1] - learningrate * der['c'])
  J.append(cost(x, y, {"m": m[-1], "c": c[-1]}))
  # print(len(J), m[-1], c[-1], J[-1], get_del_J())
  print('.', end='')
  sys.stdout.flush()
  if line:
    line[0].remove()
  line = plt.plot(x, [model(xi,{"m": m[-1], "c": c[-1]}) for xi in x], '-', color="green")
  plt.pause(0.001)

print('')
print(f"Algorithm terminated with\n  {len(J)} iterations,\n  cost {J[-1]},\n  m {m[-1]},\n  c {c[-1]}")


##### sklearn #####
x = diabetes.data[:, np.newaxis, 2]
y = diabetes.target[:]

# split into training/testing

# create linear regression model
regrmodel = linear_model.LinearRegression()

# train the model
regrmodel.fit(x, y)

# get predicted y
y_pred = regrmodel.predict(x)

plt.figure()
plt.scatter(x, y, color='red')
plt.plot(x, y_pred, '-', color="green", linewidth=3)

print('sklearn')
print(f'  m {regrmodel.coef_}')
print(f'  c {regrmodel.intercept_}')
skcost = cost(x[:,0], y, {'m': regrmodel.coef_, 'c': regrmodel.intercept_})
print(f'  cost: {skcost}')


plt.ioff()
plt.show()