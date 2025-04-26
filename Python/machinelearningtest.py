# Importando as bibliotecas necessárias
import numpy as np
from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score

# Carregar o dataset Iris
iris = datasets.load_iris()
X = iris.data  # Características (sepal length, sepal width, petal length, petal width)
y = iris.target  # Rótulos (0, 1, 2 -> três tipos de flores)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizar os dados para melhorar o desempenho do modelo
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treinar um modelo SVM (Support Vector Machine)
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Fazer previsões com o modelo
y_pred = model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'A precisão do modelo é: {accuracy * 100:.2f}%')
