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

from sklearn.model_selection import train_test_split
for dt in [iris, diabetes]:
  x_train, x_test, y_train, y_test = train_test_split(dt['attributes'], dt['target'], test_size=0.2, random_state=1)
  dt['train'] = {'attributes': x_train, 'target': y_train}
  dt['test'] = {'attributes': x_test, 'target': y_test}

#Classification
from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier(5)

input_columns = iris['attributes'].columns[:2].tolist()
x_train = iris['train']['attributes'][input_columns]
y_train = iris['train']['target'].species
knc.fit(x_train, y_train)

x_test = iris['test']['attributes'][input_columns]
y_test = iris['test']['target'].species
y_predict = knc.predict(x_test)

print(pd.DataFrame(list(zip(y_test,y_predict)), columns=['target', 'predicted']))
print(f'Accuracy: {knc.score(x_test,y_test):.4f}')

#Visualisation
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap

colormap = cm.tab20
cm_dark = ListedColormap(colormap.colors[::2])
cm_light = ListedColormap(colormap.colors[1::2])

import numpy as np
x_min = iris['attributes'][input_columns[0]].min()
x_max = iris['attributes'][input_columns[0]].max()
x_range = x_max - x_min
x_min = x_min - 0.1 * x_range
x_max = x_max + 0.1 * x_range
y_min = iris['attributes'][input_columns[1]].min()
y_max = iris['attributes'][input_columns[1]].max()
y_range = y_max - y_min
y_min = y_min - 0.1 * y_range
y_max = y_max + 0.1 * y_range
xx, yy = np.meshgrid(np.arange(x_min, x_max, .01*x_range), 
                    np.arange(y_min, y_max, .01*y_range))
z = knc.predict(list(zip(xx.ravel(), yy.ravel())))
z = z.reshape(xx.shape)

plt.figure(figsize=[12,8])
plt.pcolormesh(xx, yy, z, cmap=cm_light)

plt.scatter(x_train[input_columns[0]], x_train[input_columns[1]], 
            c=y_train, label='Training data', cmap=cm_dark, 
            edgecolor='black', linewidth=1, s=150)
plt.scatter(x_test[input_columns[0]], x_test[input_columns[1]], 
            c=y_test, marker='*', label='Testing data', cmap=cm_dark, 
            edgecolor='black', linewidth=1, s=150)
plt.xlabel(input_columns[0])
plt.ylabel(input_columns[1])
plt.legend()
plt.show()

k_list = []
accuracy_list = []
for k in range(1, len(x_train)+1):
    k_list.append(k)
    knc = KNeighborsClassifier(k)
    knc.fit(x_train, y_train)
    accuracy_list.append(knc.score(x_test, y_test))
plt.figure()
plt.scatter(k_list, accuracy_list)
plt.xlabel('$k$')
plt.ylabel('Accuracy')
plt.show()