import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:/Users/Kenjee/Documents/GitHub/E-Commerce-Sales-Analytics-Dashboard/data/churn_features.csv')
print(f'The size of the dataset is {len(df)} rows and {len(df.columns)} columns.')
print(df.head())


# Step 1: Creating the churn label
df['churn'] = np.where(df['days_since_last_order'] > 90, 1, 0)
print(df['churn'].value_counts())


# Step 2: Select Features & Target
X = df[['days_since_last_order', 'total_orders', 'total_spent']]
y = df['churn']


# Step 3: Split Data into Train/Test Sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Step 4: Train a Classifier (Random Forest)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Step 5: Evaluate the Model
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

y_pred = model.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))

# Plot confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# Step 6: Visualize Feature Importance
importances = model.feature_importances_
features = X.columns

plt.barh(features, importances)
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance")
plt.show()


# Step 7: Visualize Churn Risk
probs = model.predict_proba(X_test)[:, 1]  # Probability of churn (class = 1)
plt.hist(probs, bins=10, edgecolor='black')
plt.title('Predicted Churn Probability Distribution')
plt.xlabel('Churn Probability')
plt.ylabel('Number of Customers')
plt.show()

results = X_test.copy()
results['actual_churn'] = y_test
results['predicted_churn'] = model.predict(X_test)
results['churn_probability'] = probs

results.to_csv('"C:\Users\Kenjee\Documents\GitHub\E-Commerce-Sales-Analytics-Dashboard\data\churn_predictions.csv', index=False)
print(results.head())