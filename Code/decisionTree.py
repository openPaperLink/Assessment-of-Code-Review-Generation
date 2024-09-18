import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from collections import Counter

file_path = 'path2dataset.csv'  
data = pd.read_csv(file_path)


X = data.iloc[:,1]  
y = data.iloc[:,0] 

if isinstance(X, pd.Series):
    X = X.to_frame()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=30)

smote = SMOTE(random_state=30)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

clf = DecisionTreeClassifier()

clf.fit(X_train_resampled, y_train_resampled)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)