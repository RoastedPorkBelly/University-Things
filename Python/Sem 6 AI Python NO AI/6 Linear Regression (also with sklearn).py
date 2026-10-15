import sys
from sklearn import datasets, linear_model
import pandas as pd
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()
dt = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.DataFrame(diabetes.target, columns=['target'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dt, y, train_size=0.8, test_size=0.2)

def model(x, m, c):
    return m * x + c

def cost(y, yh):
    return ((y-yh)**2).mean()

def derivatives(x,y,yh):
    return{
        "m": ((y-yh)*x).mean()*-2,
        "c": (y-yh).mean()*-2
    }

learningrate = 0.3
m = []
c = []
J = []
m.append(0)
c.append(0)
J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))

J_min = 0.01
del_J_min = 0.0000000001
max_iter = 50000

plt.ion()  # FIX: added so live graph updating works
plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.title('Training data')
plt.xlabel('BMI')
line = None

while True:
    if J[-1] < J_min: break
    if len(J) > 1 and abs(J[-1]-J[-2])/J[-2] < del_J_min: break
    if len(J) >= max_iter: break
    yh = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
    d  = derivatives(X_train['bmi'], y_train['target'], yh)
    m.append(m[-1] - learningrate * d['m'])
    c.append(c[-1] - learningrate * d['c'])
    J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))
    if line:
        line[0].remove()
    # FIX: line is now drawn every iteration, not just after the first
    line = plt.plot(X_train['bmi'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])), '-', color='green')
    plt.pause(0.001)
    print('.', end='')
    sys.stdout.flush()

y_train_pred = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
y_test_pred = X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
print('\nAlgorithm terminated with')
print(f'  {len(J)} iterations,')
print(f'  m {m[-1]}')
print(f'  c {c[-1]}')
print(f'  training cost {J[-1]}')
testcost = cost(y_test['target'], y_test_pred)
print(f'  testing cost {testcost}')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], \
         X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1])), \
         '-', color='green')
plt.title('Testing data')

# --- sklearn section (from 6b.py) ---
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

plt.ioff()   # FIX: added so graphs stay open
plt.show()   # FIX: added so graphs actually display
