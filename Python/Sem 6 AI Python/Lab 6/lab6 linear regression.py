from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
from math import fabs, inf
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
dt = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.DataFrame(diabetes.target, columns=['target'])

X_train, X_test, y_train, y_test = train_test_split(dt, y, test_size=0.2)

def model(x, m, c):
  return m*x + c

def cost(y, yh):
  return ((y-yh)**2).mean()

def derivatives(x, y, yh):
  return {
    'm': ((y-yh)*x).mean()*-2,
    'c': (y-yh).mean()*-2
  }

# initial values
learningrate = 0.1
m = []
c = []
J = []
m.append(0)
c.append(0)
J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))

# termination conditions
J_min = 0.01
del_J_min = 0.0001
max_iter = 10000

def getdelJ():
  if len(J) > 1:
    return fabs(J[-1] - J[-2])/J[-1]
  else:
    return inf

plt.ion()

plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.title('Training data')
plt.xlabel('BMI')
line = None
while J[-1] > J_min and getdelJ() > del_J_min and len(J) < max_iter:
  der = derivatives(X_train['bmi'], y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])))
  m.append(m[-1] - learningrate * der['m'])
  c.append(c[-1] - learningrate * der['c'])
  J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))

  print('.', end='')
  sys.stdout.flush()

  if line:
    line[0].remove()
  line = plt.plot(X_train['bmi'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])), '-', color='green')
  plt.pause(0.001)

y_train_pred = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
y_test_pred = X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
print('\nAlgorithm terminated with')
print(f'  {len(J)} iterations')
print(f'  m {m[-1]}')
print(f'  c {c[-1]}')
print(f'  training cost {J[-1]}')
testcost = cost(y_test['target'], y_test_pred)
print(f'  testing cost {testcost}')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], y_test_pred, '-', color='green')
plt.title('Testing data')


##### sklearn
regrmodel = linear_model.LinearRegression()
regrmodel.fit(X_train[['bmi']], y_train['target'])
y_train_pred = regrmodel.predict(X_train[['bmi']])
y_test_pred = regrmodel.predict(X_test[['bmi']])

y_train_pred = pd.Series(y_train_pred)
y_train_pred.index = y_train.index

y_test_pred = pd.Series(y_test_pred)
y_test_pred.index = y_test.index

print('sklearn')
print(f'  m {regrmodel.coef_}')
print(f'  c {regrmodel.intercept_}')
traincost = cost(y_train['target'], y_train_pred)
testcost = cost(y_test['target'], y_test_pred)
print(f'  training cost: {traincost}')
print(f'  testing cost: {testcost}')

plt.figure()
plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.plot(X_train['bmi'], y_train_pred, '-', color='green')
plt.title('Training data (sklearn)')
plt.xlabel('BMI')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], y_test_pred, '-', color='green')
plt.title('Testing data (sklearn)')
plt.xlabel('BMI')


##### multivariate linear regression
regrmodel = linear_model.LinearRegression()
regrmodel.fit(X_train[['bmi','bp']], y_train['target'])
y_train_pred = regrmodel.predict(X_train[['bmi','bp']])
y_test_pred = regrmodel.predict(X_test[['bmi','bp']])

y_train_pred = pd.Series(y_train_pred)
y_train_pred.index = y_train.index

y_test_pred = pd.Series(y_test_pred)
y_test_pred.index = y_test.index

print('sklearn')
print(f'  m {regrmodel.coef_}')
print(f'  c {regrmodel.intercept_}')
traincost = cost(y_train['target'], y_train_pred)
testcost = cost(y_test['target'], y_test_pred)
print(f'  training cost: {traincost}')
print(f'  testing cost: {testcost}')

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train['bmi'], X_train['bp'], y_train['target'], color='red')
ax.scatter(X_train['bmi'], X_train['bp'], y_train_pred, color='green')
ax.set_xlabel('BMI')
ax.set_ylabel('Blood pressure')
ax.set_title('Training data (sklearn multivariate)')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_test['bmi'], X_test['bp'], y_test['target'], color='red')
ax.scatter(X_test['bmi'], X_test['bp'], y_test_pred, color='green')
ax.set_xlabel('BMI')
ax.set_ylabel('Blood pressure')
ax.set_title('Testing data (sklearn multivariate)')


plt.ioff()
plt.show()
  