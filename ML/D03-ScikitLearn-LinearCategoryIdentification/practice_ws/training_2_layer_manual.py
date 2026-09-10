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

def numerify(df, columns):
    for column in columns:
        df[column] = (df[column] == "Yes")


def first_layer(X_train, y_train):

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
    return model

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
    
    X = df[list(set(df.columns.to_list()) - set(target_column))]
    y = df[target_column[0]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=28, stratify=X["InternetSeniorContract"]
    )
    
    model = first_layer(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_train_pred_prob = model.predict_proba(X_train)
    print("Training Metric:")
    report(y_train, y_train_pred)


    y_test_pred = model.predict(X_test)
    print("Test Metric:")
    report(y_test, y_test_pred)

    df2 = pd.concat([X_train, y_train], axis=1)
    df2["Pred_Churn"] = y_train_pred
    df2["Pred_Churn_Prod"] = y_train_pred_prob[:, 1]
    df2 = df2[df2["Pred_Churn"] == "Yes"]
    print(df2)
    df2.to_csv('Remainder_for_Model2.csv',index=False, sep=',')
    






    



   


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
