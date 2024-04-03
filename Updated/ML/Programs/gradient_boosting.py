import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix,classification_report

df = pd.read_csv("../URL_data.csv")
X =  df.drop(columns=['target'])
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize gradient boosting model
gradient_boosting_model = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Train gradient boosting model
gradient_boosting_model.fit(X_train, y_train)

# Model evaluation for gradient boosting
y_pred = gradient_boosting_model.predict(X_test)
print("Confusion Matrix:",confusion_matrix(y_test, y_pred))
print(f'Classification Report\n {classification_report(y_test,y_pred)}')