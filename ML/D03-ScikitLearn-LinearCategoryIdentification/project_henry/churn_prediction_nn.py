from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split, FixedThresholdClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
from fourier_features import FourierFeatures
from group_features import GroupInteraction
from plot_roc import plot_precision_vs_recall, plot_roc

def find_cost(x, y, y_pred_prob, threshold):
    combined = x.copy()
    combined['Churn'] = y
    combined['pred_prob'] = y_pred_prob
    combined['pred_churn'] = np.where(combined['pred_prob'] >= threshold, "Yes", "No")
    combined['cost'] = np.select([
        (combined['Churn'] == "Yes") & (combined['pred_churn'] == "No"),
        (combined['Churn'] == "No") & (combined['pred_churn'] == "Yes")
    ], [
        combined["MonthlyCharges"],
        20 
    ],
    default=0)
    return combined["cost"].sum()

def find_minimum_cost(x, y, y_pred_prob):
    min_cost = 1e100
    min_cost_threshold = -1
    for threshold in range(0, 101):
        cost = find_cost(x, y, y_pred_prob, threshold/100)
        if cost < min_cost:
            min_cost = cost
            min_cost_threshold = threshold
    return min_cost, min_cost_threshold

def find_gain(x, y, y_pred_prob, threshold):
    combined = x.copy()
    combined['Churn'] = y
    combined['pred_prob'] = y_pred_prob
    combined['pred_churn'] = np.where(combined['pred_prob'] >= threshold, "Yes", "No")
    combined['gain'] = np.select([
        (combined['Churn'] == "Yes") & (combined['pred_churn'] == "Yes"),
        (combined['Churn'] == "No") & (combined['pred_churn'] == "Yes")
    ], [
        combined["MonthlyCharges"] * 0.7,
        -20 
    ],
    default=0)
    return combined["gain"].sum()

def find_max_gain(x, y, y_pred_prob):
    max_gain = -1e100
    max_gain_threshold = -1
    for threshold in range(0, 101):
        gain = find_gain(x, y, y_pred_prob, threshold/100)
        if gain > max_gain:
            max_gain = gain
            max_gain_threshold = threshold
    return max_gain, max_gain_threshold


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df["TotalCharges"] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df["TotalCharges"] = df["TotalCharges"].fillna(0)
df["tenure2"] = df["tenure"] * df["tenure"]
df["tenure3"] = df["tenure2"] * df["tenure"]
df["MonthlyCharges2"] = df["MonthlyCharges"] * df["MonthlyCharges"]
df["MonthlyCharges3"] = df["MonthlyCharges2"] * df["MonthlyCharges"]
df["ContractInternet"] = df["Contract"] + df["InternetService"]
df["ContractPayment"] = df["Contract"] + df["PaymentMethod"]

numeric_features = [
    "tenure",
    'TotalCharges',
    'MonthlyCharges'
]

categorical_features = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
    'PaymentMethod',
]

X = df[numeric_features + categorical_features]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle=True, random_state=5)

sample_weights = np.where(y_train == "Yes", X_train["MonthlyCharges"] / 20, 1)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

two_layer_nn = MLPClassifier(
    hidden_layer_sizes=(16, 8 ),  # One hidden layer with 16 neurons
    activation='logistic',     # Sigmoid activation function for the hidden layer
    solver='adam',             # Optimization algorithm 
    max_iter=1000,
    random_state=42,
    #alpha = 1.7
)

feature_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("regressor", two_layer_nn)
    ]
)

model = feature_pipeline

model.fit(X_train, y_train, 
          regressor__sample_weight=sample_weights
        )

y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)
y_pred_prob_train = model.predict_proba(X_train)

print(y_pred_prob)
print(find_cost(X_test, y_test, y_pred_prob[:,1], 0.5))
print(find_minimum_cost(X_test, y_test, y_pred_prob[:,1]))
print(find_minimum_cost(X_train, y_train, y_pred_prob_train[:,1]))

print("Counts:\n", confusion_matrix(y_test, y_pred))
print("Precision per class (normalize='pred'):\n", confusion_matrix(y_test, y_pred, normalize="pred").round(3))
print("Recall per class (normalize='true'):\n", confusion_matrix(y_test, y_pred, normalize="true").round(3))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred, pos_label="Yes"))

plot_roc(y_pred_prob[:,1], y_test, positive_label="Yes")
plot_precision_vs_recall(y_pred_prob[:,1], y_test, positive_label="Yes")
plt.show()
