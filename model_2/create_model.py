import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv('datasets/datasets.csv')

# Split the dataset into features and labels
X = df[['death', 'injuries', 'property_large', 'property_medium', 'property_small', 'keyword']]
y = df['label']

# Initialize the Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Initialize KFold with 5 splits (each fold is 20%)
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform k-fold cross-validation and evaluate the model
accuracies = cross_val_score(clf, X, y, cv=kf, scoring='accuracy')

# Train the model on the entire dataset
clf.fit(X, y)

# Print the highest accuracy
highest_accuracy = max(accuracies)
print(f'Highest Accuracy: {highest_accuracy}')

# Optionally, print the mean accuracy
print(f'Mean Accuracy: {accuracies.mean()}')

# Store the model with the highest accuracy into a joblib file
joblib.dump(clf, 'models/best_decision_tree_model.joblib')
print("Successfully save the model to models/best_decision_tree_model.joblib")