import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.neural_network import MLPClassifier

df = pd.read_csv("../URL_data.csv")
X =  df.drop(columns=['target'])
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu', solver='adam', random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Confusion Matrix:",confusion_matrix(y_test, y_pred))
print(f'Classification Report\n {classification_report(y_test,y_pred)}')