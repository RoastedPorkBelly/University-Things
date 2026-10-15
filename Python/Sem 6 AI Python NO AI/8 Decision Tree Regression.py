#import datasets
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
iris = {
  'attributes': pd.DataFrame(iris.data, columns=iris.feature_names),
  'target': pd.DataFrame(iris.target, columns=['species']),
  'targetNames': iris.target_names
}
diabetes = datasets.load_diabetes()
diabetes = {
  'attributes': pd.DataFrame(diabetes.data, columns=diabetes.feature_names),
  'target': pd.DataFrame(diabetes.target, columns=['diseaseProgression'])
}

#split
from sklearn.model_selection import train_test_split
for dt in [iris, diabetes]:
  x_train, x_test, y_train, y_test = train_test_split(dt['attributes'], dt['target'], test_size=0.2, random_state=1)
  dt['train'] = {'attributes': x_train, 'target': y_train}
  dt['test'] = {'attributes': x_test, 'target': y_test}

#regression
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()

#training
dtr.fit(diabetes['train']['attributes'], diabetes['train']['target'])

#prediction
predicts = dtr.predict(diabetes['test']['attributes'])

#target and prediction comparison
print(pd.DataFrame(list(zip(diabetes['test']['target'].diseaseProgression,predicts)), columns=['target', 'predicted']))
accuracy = dtr.score(diabetes['test']['attributes'],
                    diabetes['test']['target'].diseaseProgression)
print(f'Accuracy: {accuracy:.4f}')


## loop of comparing accuracy for different max depth
import matplotlib.pyplot as plt
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


#Visualization
from sklearn.tree import plot_tree
plt.figure(figsize=[10,10])
tree = plot_tree(dtr, feature_names=diabetes['attributes'].columns.tolist(), 
                filled=True, rounded=True)

dtr = DecisionTreeRegressor()
input_cols = ['age', 'bmi']
dtr.fit(diabetes['train']['attributes'][input_cols], 
        diabetes['train']['target'].diseaseProgression)

#plot decision surface
plt.figure(figsize=[50,50])
plot_tree(dtr, feature_names=input_cols, filled=True, rounded=True)
plt.savefig('regressionDecisionTreeWithNoMaxDepth.png')

#colormap
from matplotlib import cm
dia_cm = cm.Reds

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

#max depth 3
dtr = DecisionTreeRegressor(max_depth=3)
input_cols = ['age', 'bmi']
dtr.fit(diabetes['train']['attributes'][input_cols], 
        diabetes['train']['target'].diseaseProgression)

plt.figure(figsize=[50,50])
plot_tree(dtr, feature_names=input_cols, filled=True, rounded=True)
plt.savefig('regressionDecisionTreeWithMaxDepth3.png')

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

#plot decision surface
plt.figure()
plt.pcolormesh(xx, yy, z, cmap=dia_cm)

#plot training and test data
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
train_acc = dtr.score(diabetes['train']['attributes'][input_cols],
                      diabetes['train']['target'].diseaseProgression)
test_acc = dtr.score(diabetes['test']['attributes'][input_cols],
                    diabetes['test']['target'].diseaseProgression)
plt.title(f'training: {train_acc:.3f}, testing: {test_acc:.3f}')
plt.xlabel(input_cols[0])
plt.ylabel(input_cols[1])
plt.legend()
plt.colorbar()
plt.show()