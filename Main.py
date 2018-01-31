import Functions
data = Functions.getInput()
target = Functions.getOutput()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size= 0.1, random_state=27)


from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(30, 20, 10), max_iter=300, solver='adam', random_state=1)

mlp.fit(x_train, y_train)
predict = mlp.predict(x_test)


from sklearn import metrics
print(metrics.accuracy_score(y_test, predict))