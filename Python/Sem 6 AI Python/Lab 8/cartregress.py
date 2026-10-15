# dataset
from sklearn import datasets
import pandas as pd
diabetes = datasets.load_diabetes()
diabetes = {
  'attributes': pd.DataFrame(diabetes.data, columns=diabetes.feature_names),
  'target': pd.DataFrame(diabetes.target, columns=['diseaseProgression'])
}

# split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(diabetes['attributes'], diabetes['target'], test_size=0.2, random_state=1)
diabetes['train'] = {
  'attributes': x_train,
  'target': y_train
}
diabetes['test'] = {
  'attributes': x_test,
  'target': y_test
}

# regression
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()

## training
dtr.fit(diabetes['train']['attributes'], diabetes['train']['target'])

## predicting
predicts = dtr.predict(diabetes['test']['attributes'])

## comparing predicted and target
print(pd.DataFrame(list(zip(diabetes['test']['target'].diseaseProgression, predicts)), columns=['target', 'predicted']))
accuracy = dtr.score(diabetes['test']['attributes'], diabetes['test']['target'].diseaseProgression)
print(f'Accuracy: {accuracy:.4f}')

## visualisation of decision tree
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=[10,10])
tree = plot_tree(dtr, feature_names=diabetes['attributes'].columns.tolist(), filled=True, rounded=True)
# plt.show()

## loop of comparing accuracy for different max depth
max_depths = [1,2,3,5,7,20]
training_accuracy = []
testing_accuracy = []
for md in max_depths:
  dtr = DecisionTreeRegressor(max_depth=md)
  dtr.fit(diabetes['train']['attributes'], diabetes['train']['target'].diseaseProgression)
  train = dtr.score(diabetes['train']['attributes'], diabetes['train']['target'].diseaseProgression)
  test = dtr.score(diabetes['test']['attributes'], diabetes['test']['target'].diseaseProgression)
  training_accuracy.append(train)
  testing_accuracy.append(test)
plt.figure()
plt.scatter(max_depths, training_accuracy, label='training accuracy')
plt.scatter(max_depths, testing_accuracy, label='testing accuracy')
plt.xlabel('max depth')
plt.ylabel('accuracy')
plt.legend()

# plt.show()

## visualisation of the decision surface for max_depth=None
dtr = DecisionTreeRegressor()
input_cols = ['age', 'bmi']
dtr.fit(diabetes['train']['attributes'][input_cols], diabetes['train']['target'].diseaseProgression)

plt.figure(figsize=[150,150])
plot_tree(dtr, feature_names=input_cols, filled=True, rounded=True)
plt.savefig('regressionDecisionTreeWithNoMaxDepth.png')
plt.close()

### colormaps
from matplotlib import cm
dia_cm = cm.get_cmap('Reds')

### calculating the decision surface
import numpy as np
x_min = diabetes['attributes'][input_cols[0]].min()
x_max = diabetes['attributes'][input_cols[0]].max()
x_range = x_max - x_min
x_min = x_min - 0.1 * x_range
x_max = x_max + 0.1 * x_range
y_min = diabetes['attributes'][input_cols[1]].min()
y_max = diabetes['attributes'][input_cols[1]].max()
y_range = y_max - y_min
y_min = y_min - 0.1 * y_range
y_max = y_max + 0.1 * y_range
xx, yy = np.meshgrid(np.arange(x_min, x_max, .01*x_range),
                     np.arange(y_min, y_max, .01*y_range))
z = dtr.predict(list(zip(xx.ravel(), yy.ravel())))
z = z.reshape(xx.shape)

### plot the decision surface
plt.figure()
plt.pcolormesh(xx, yy, z, cmap=dia_cm)

### plot the training and testing data
plt.scatter(diabetes['train']['attributes'][input_cols[0]],
            diabetes['train']['attributes'][input_cols[1]],
            c=diabetes['train']['target'].diseaseProgression,
            label='Training data', cmap=dia_cm,
            edgecolor='black', linewidth=1, s=150)
plt.scatter(diabetes['test']['attributes'][input_cols[0]],
            diabetes['test']['attributes'][input_cols[1]],
            c=diabetes['test']['target'].diseaseProgression, marker='*',
            label='Testing data', cmap=dia_cm,
            edgecolor='black', linewidth=1, s=150)
plt.xlabel(input_cols[0])
plt.ylabel(input_cols[1])
plt.legend()
plt.colorbar()
# plt.show()

## visualisation of the decision surface for max_depth=3
dtr = DecisionTreeRegressor(max_depth=3)
input_cols = ['age', 'bmi']
dtr.fit(diabetes['train']['attributes'][input_cols], diabetes['train']['target'].diseaseProgression)

plt.figure(figsize=[50,50])
plot_tree(dtr, feature_names=input_cols, filled=True, rounded=True)
plt.savefig('regressionDecisionTreeWithMaxDepth3.png')
plt.close()

### colormaps
from matplotlib import cm
dia_cm = cm.get_cmap('Reds')

### calculating the decision surface
import numpy as np
x_min = diabetes['attributes'][input_cols[0]].min()
x_max = diabetes['attributes'][input_cols[0]].max()
x_range = x_max - x_min
x_min = x_min - 0.1 * x_range
x_max = x_max + 0.1 * x_range
y_min = diabetes['attributes'][input_cols[1]].min()
y_max = diabetes['attributes'][input_cols[1]].max()
y_range = y_max - y_min
y_min = y_min - 0.1 * y_range
y_max = y_max + 0.1 * y_range
xx, yy = np.meshgrid(np.arange(x_min, x_max, .01*x_range),
                     np.arange(y_min, y_max, .01*y_range))
z = dtr.predict(list(zip(xx.ravel(), yy.ravel())))
z = z.reshape(xx.shape)

### plot the decision surface
plt.figure()
plt.pcolormesh(xx, yy, z, cmap=dia_cm)

### plot the training and testing data
plt.scatter(diabetes['train']['attributes'][input_cols[0]],
            diabetes['train']['attributes'][input_cols[1]],
            c=diabetes['train']['target'].diseaseProgression,
            label='Training data', cmap=dia_cm,
            edgecolor='black', linewidth=1, s=150)
plt.scatter(diabetes['test']['attributes'][input_cols[0]],
            diabetes['test']['attributes'][input_cols[1]],
            c=diabetes['test']['target'].diseaseProgression, marker='*',
            label='Testing data', cmap=dia_cm,
            edgecolor='black', linewidth=1, s=150)
plt.xlabel(input_cols[0])
plt.ylabel(input_cols[1])
plt.legend()
plt.colorbar()
plt.show()