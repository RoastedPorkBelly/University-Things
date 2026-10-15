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

#classification decision tree
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion='gini')

#training
dtc.fit(iris['train']['attributes'], iris['train']['target'])

#predicting
predicts = dtc.predict(iris['test']['attributes'])

#comparison of target and prediction
print(pd.DataFrame(list(zip(iris['test']['target'].species,predicts)), columns=['target', 'predicted']))
accuracy = dtc.score(iris['test']['attributes'],iris['test']['target'].species)
print(f'Accuracy: {accuracy:.4f}')

#Visualization
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=[10,10])
tree = plot_tree(dtc, feature_names=iris['attributes'].columns.tolist(),
                 class_names=iris['targetNames'],
                 filled=True,
                 rounded=True,
                 )
plt.show()

# Compare accuracy with different max depths loop
depths = [1, 2, 3, 5, 7, 20]
train_scores = []
test_scores = []

for depth in depths:
    model = DecisionTreeClassifier(criterion='gini', max_depth=depth, random_state=1)
    model.fit(iris['train']['attributes'], iris['train']['target'])
    train_acc = model.score(iris['train']['attributes'], iris['train']['target'].species)
    test_acc = model.score(iris['test']['attributes'], iris['test']['target'].species)
    train_scores.append(train_acc)
    test_scores.append(test_acc)
    print(f'max_depth={depth} | train={train_acc:.4f} | test={test_acc:.4f}')

plt.figure()
plt.plot(depths, train_scores, marker='o', label='Training accuracy')
plt.plot(depths, test_scores, marker='o', label='Testing accuracy')
plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.xticks(depths)
plt.legend()
plt.show()

#Visualization of decision surface for unlimited depth
dtc = DecisionTreeClassifier()
input_cols = iris['train']['attributes'].columns[:2].tolist()
dtc.fit(iris['train']['attributes'][input_cols], iris['train']['target'].species)

plt.figure(figsize=[50,50])
plot_tree(dtc, feature_names=input_cols, 
          class_names=iris['targetNames'], filled=True, rounded=True)
plt.savefig('classificationDecisionTreeWithNoMaxDepth.png')

### colormaps
from matplotlib import cm
from matplotlib.colors import ListedColormap
colormap = cm.tab20
cm_dark = ListedColormap(colormap.colors[::2])
cm_light = ListedColormap(colormap.colors[1::2])

### calculating the decision surface
import numpy as np
x_min = iris['attributes'][input_cols[0]].min()
x_max = iris['attributes'][input_cols[0]].max()
x_range = x_max - x_min
x_min = x_min - 0.1 * x_range
x_max = x_max + 0.1 * x_range
y_min = iris['attributes'][input_cols[1]].min()
y_max = iris['attributes'][input_cols[1]].max()
y_range = y_max - y_min
y_min = y_min - 0.1 * y_range
y_max = y_max + 0.1 * y_range
xx, yy = np.meshgrid(np.arange(x_min, x_max, .01*x_range), 
                    np.arange(y_min, y_max, .01*y_range))
z = dtc.predict(list(zip(xx.ravel(), yy.ravel())))
z = z.reshape(xx.shape)

### plot the training and testing data
plt.figure()
plt.pcolormesh(xx, yy, z, cmap=cm_light)

plt.scatter(iris['train']['attributes'][input_cols[0]],   
            iris['train']['attributes'][input_cols[1]], 
            c=iris['train']['target'].species, cmap=cm_dark, s=200,
            label='Training data', edgecolor='black', linewidth=1)
plt.scatter(iris['test']['attributes'][input_cols[0]], 
            iris['test']['attributes'][input_cols[1]], 
            c=iris['test']['target'].species, cmap=cm_dark, s=200,
            label='Testing data', edgecolor='black', linewidth=1,
            marker='*')
train_acc = dtc.score(iris['train']['attributes'][input_cols], 
                      iris['train']['target'].species)
test_acc = dtc.score(iris['test']['attributes'][input_cols], 
                    iris['test']['target'].species)
plt.title(f'training: {train_acc:.3f}, testing: {test_acc:.3f}')
plt.xlabel(input_cols[0])
plt.ylabel(input_cols[1])
plt.legend()
plt.show()

# Pruned decision tree with max_depth=3
dtc = DecisionTreeClassifier(max_depth=3)
dtc.fit(iris['train']['attributes'][input_cols], iris['train']['target'].species)

plt.figure(figsize=[50,50])
plot_tree(dtc, feature_names=input_cols,
          class_names=iris['targetNames'], filled=True, rounded=True)
plt.savefig('classificationDecisionTreeWithMaxDepth3.png')

z = dtc.predict(list(zip(xx.ravel(), yy.ravel())))
z = z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, z, cmap=cm_light)

plt.scatter(iris['train']['attributes'][input_cols[0]],
            iris['train']['attributes'][input_cols[1]],
            c=iris['train']['target'].species, cmap=cm_dark, s=200,
            label='Training data', edgecolor='black', linewidth=1)
plt.scatter(iris['test']['attributes'][input_cols[0]],
            iris['test']['attributes'][input_cols[1]],
            c=iris['test']['target'].species, cmap=cm_dark, s=200,
            label='Testing data', edgecolor='black', linewidth=1,
            marker='*')
train_acc = dtc.score(iris['train']['attributes'][input_cols],
                      iris['train']['target'].species)
test_acc = dtc.score(iris['test']['attributes'][input_cols],
                    iris['test']['target'].species)
plt.title(f'training: {train_acc:.3f}, testing: {test_acc:.3f}')
plt.xlabel(input_cols[0])
plt.ylabel(input_cols[1])
plt.legend()
plt.show()