import Functions

data = Functions.getInput()
target = Functions.getOutput()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.1)


from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import numpy as np

mlp = MLPClassifier(hidden_layer_sizes=(30, 20, 10), max_iter=200, solver='adam')
mlp.fit(x_train, y_train)
predict = mlp.predict(x_test)
print(metrics.accuracy_score(y_test, predict))
print(metrics.confusion_matrix(np.argmax(a=y_test.values, axis=1), np.argmax(a=predict, axis=1)))