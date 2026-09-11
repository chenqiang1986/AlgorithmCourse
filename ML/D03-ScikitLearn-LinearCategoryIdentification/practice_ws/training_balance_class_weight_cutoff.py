from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import FixedThresholdClassifier, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from plot_graphs import report_precision_recall
from plot_roc import plot_precision_vs_recall

def main():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'], 
        errors='coerce').fillna(0)
    
    target_column = ['Churn']

    numeric_columns = [
        'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen'
    ]

    category_columns = [
        'gender', 'Partner', 'Dependents',
        'PhoneService', 
        'MultipleLines', 

        'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod',
    ]

    feature_columns = numeric_columns + category_columns

    X = df[feature_columns]
    y = df[target_column[0]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=32, stratify=y
    )

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), category_columns),
            ("num", StandardScaler(), numeric_columns),
        ]
    )

    regressor=FixedThresholdClassifier(
        estimator=LogisticRegression(
            class_weight="balanced"
        ),
        threshold=0.48,
    )

    model = model = Pipeline(
            [
                ("preprocess", preprocessor),
                ("regressor", regressor),
            ]
        )

    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_train_pred_prob = model.predict_proba(X_train)[:, 1]
    report_precision_recall(y_train, y_train_pred, "Training Metric")
    plot_precision_vs_recall(y_train_pred_prob, y_train, "Yes", title="Training Precision vs Recall")


    y_test_pred = model.predict(X_test)
    y_test_pred_prob = model.predict_proba(X_test)[:, 1]
    report_precision_recall(y_test, y_test_pred, "Test Metric")
    plot_precision_vs_recall(y_test_pred_prob, y_test, "Yes", title="Test Precision vs Recall")

    plt.show()
    






    



   


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
