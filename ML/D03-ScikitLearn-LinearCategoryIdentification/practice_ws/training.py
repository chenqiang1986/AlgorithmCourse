import pandas as pd
import numpy as np
import math
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def report(true_value, pred_value):
    accuracy = accuracy_score(true_value, pred_value)    
    print("  Accuracy:", accuracy,"\n")
    print("  Confusion Matrix Count:")
    print(confusion_matrix(true_value, pred_value),"\n")

    print("  Confusion Matrix Normalize on Actual:")
    print("  [Recall_Neg, 1-Recall_Neg]")
    print("  [1-Recall_Pos, Recall_Pos]")
    print(confusion_matrix(true_value, pred_value, normalize="true"),"\n")

    print("  Confusion Matrix Normalize on Prediction:")
    print("  [Precision_Neg, 1-Precision_Pos]")
    print("  [1-Precision_Neg, Precision_Pos]")
    print(confusion_matrix(true_value, pred_value, normalize="pred"),"\n")

    print(classification_report(true_value, pred_value))

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
        'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod',
    ]

    feature_columns = numeric_columns + category_columns

    X = df[feature_columns]
    y = df[target_column[0]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=22,
    )

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), category_columns),
            ("num", StandardScaler(), numeric_columns),
        ]
    )

    regressor=LogisticRegression()

    model = model = Pipeline(
            [
                ("preprocess", preprocessor),
                ("regressor", regressor),
            ]
        )

    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    print("Training Metric:")
    report(y_train, y_train_pred)


    y_test_pred = model.predict(X_test)
    print("Test Metric:")
    report(y_test, y_test_pred)
    






    



   


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
