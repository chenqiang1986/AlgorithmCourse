import pandas as pd
import numpy as np
import math
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import FixedThresholdClassifier, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler

from fourier_features import FourierFeatures
from group_features import GroupInteraction
from plot_graphs import report_precision_recall

def numerify(df, columns):
    for column in columns:
        df[column] = (df[column] == "Yes")


def main():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'], 
        errors='coerce').fillna(0)
    
    df['ChargeRatio'] = (df['TotalCharges'] / df['tenure']).fillna(0)

    df['InternetSeniorContract'] = df['InternetService'] + df['SeniorCitizen'].astype(str) + df["Contract"]

    numerify(df, [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies',
       'PaperlessBilling', 'Dependents','Partner', 
    ])
    
    target_column = ['Churn']

    nonlinear_columns = [
        'tenure',         
        'MonthlyCharges',
        'ChargeRatio',
    ]

    grp_columns = [
         'TotalCharges',

       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 

       'PaperlessBilling','Dependents', 'Partner', 
    ]

    numeric_columns = [        

       #'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 

       #'PaperlessBilling','Dependents', 'Partner', 
    ]

    category_columns = [
       'gender',
       'MultipleLines', 
       'InternetSeniorContract',
       'PaymentMethod',
    ]

    feature_columns = numeric_columns + category_columns + grp_columns + nonlinear_columns

    X = df[feature_columns]
    y = df[target_column[0]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=28, stratify=X["InternetSeniorContract"]
    )

    nonlinearize = ColumnTransformer(
        [
            ("poly", FourierFeatures(degree=3),["tenure"]),
            ("poly2", FourierFeatures(degree=3),["MonthlyCharges"]),
            ("poly3", FourierFeatures(degree=3),["ChargeRatio"]),
        ],
        remainder = "passthrough",
        verbose_feature_names_out=False,
    ).set_output(transform="pandas")

    nonlinearize.fit(X_train)
    poly_features = nonlinearize.get_feature_names_out().tolist()
    poly_features = [f 
                        for f in poly_features 
                        if any(origin in f for origin in nonlinear_columns)
    ]
    grp_columns += poly_features
    print(grp_columns)


    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), category_columns),
            ("num", StandardScaler(), numeric_columns),
            ("grp", GroupInteraction("InternetSeniorContract"), ["InternetSeniorContract"] + grp_columns)
        ]
    )

    regressor=FixedThresholdClassifier(
        estimator=LogisticRegression(
            #max_iter=100000,
            class_weight="balanced"
        ),
        threshold=0.5,
    )

    model = model = Pipeline(
            [
                ("nonlinearize", nonlinearize),
                ("preprocess", preprocessor),
                ("regressor", regressor),
            ]
        )

    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    report_precision_recall(y_train, y_train_pred, "Training Metric")


    y_test_pred = model.predict(X_test)
    report_precision_recall(y_test, y_test_pred, "Test Metric")
    






    



   


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
