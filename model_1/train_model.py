import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from joblib import dump

from perceptron import Perceptron

# Read the dataset
df = pd.read_csv('datasets/datasets.csv')

# Split the dataset into features and labels
X = df[['region', 'bao_lu', 'dich_benh']].values
y = df['label'].values

# Initialize KFold with 10 splits
kf = KFold(n_splits=10, shuffle=True, random_state=42)

best_accuracy = 0
best_model = None

# Loop over a smaller range of iterations with larger steps

accuracies = []
    # Perform k-fold cross-validation
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Initialize and train the Perceptron model
    perceptron = Perceptron(learning_rate=0.01, n_iters=50)
    perceptron.fit(X_train, y_train)

    # Predict on the test set
    y_pred = perceptron.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Calculate the average accuracy for this number of iterations
average_accuracy = np.mean(accuracies)
print(f'Average Accuracy {average_accuracy}')

# Save the best trained model
if perceptron is not None:
    dump(perceptron, 'models/trained_perceptron_model.joblib')
print("Model trained and saved successfully!")
