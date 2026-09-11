from matplotlib import pyplot as plt
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
from plot_roc import plot_roc

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


def second_layer(X_train, y_train):


    numeric_columns = [        
        'tenure',            
        "MonthlyCharges",
        "TotalCharges",
        "ChargeRatio", 
        "Pred_Churn_Prod",        
    ]

    category_columns = [
       'gender',
       'MultipleLines', 
       'InternetSeniorContract',
       'PaymentMethod',
    ]



    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), category_columns),
            ("num", StandardScaler(), numeric_columns),
        ]
    )

    regressor=FixedThresholdClassifier(
        estimator=LogisticRegression(
            #max_iter=100000,
            class_weight="balanced"
        ),
        threshold=0.35,
    )

    model = model = Pipeline(
            [
                ("preprocess", preprocessor),
                ("regressor", regressor),
            ]
        )

    model.fit(X_train, y_train)
    return model

def attach_pred_prob(X, y, column_name_pred, y_pred, column_name_pred_prob, y_pred_prob):
    X_attached = X.copy()
    X_attached[column_name_pred] = y_pred
    X_attached[column_name_pred_prob] = y_pred_prob

    return X_attached, y

def filter_pred_yes(X, y, column_name, value):
    combined = pd.concat([X,y], axis=1)
    filtered = combined[combined[column_name]==value]

    print(filtered)
    X_filtered = filtered[X.columns]
    y_filtered = filtered[y.name]

    return X_filtered, y_filtered

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
    y_train_pred_prob = model.predict_proba(X_train)[:, 1]
    report_precision_recall(y_train, y_train_pred, "Training Metric")
    #plot_roc(y_train_pred_prob[:, 1], y_train, "Yes")
    #plot_roc(y_train_pred_prob[:, 0], y_train, "No")


    y_test_pred = model.predict(X_test)
    y_test_pred_prob = model.predict_proba(X_test)[:, 1]
    report_precision_recall(y_test, y_test_pred, "Test Metric")


    X_train_2, y_train_2 = attach_pred_prob(
        X_train, y_train, 
        "Pred_Churn", y_train_pred, 
        "Pred_Churn_Prod", y_train_pred_prob)
    X_train_2_filtered, y_train_2_filtered = filter_pred_yes(
        X_train_2, y_train_2,
        "Pred_Churn", "Yes",
    )

    model2 = second_layer(X_train_2_filtered, y_train_2_filtered) 

    y_train_2_pred = model2.predict(X_train_2)
    y_train_2_pred_prob = model2.predict_proba(X_train_2)[:, 1]

    X_train_3, y_train_3 = attach_pred_prob(
        X_train_2, y_train_2,
        "Fixed_Pred_Churn", y_train_2_pred,
        "Fixed_Pred_Churn_Prod", y_train_2_pred_prob,
    )

    # Fixed Pred Churn won't work on the the predicted No part.
    X_train_3["Final_Churn_Pred"] = np.where(X_train_3["Pred_Churn"] == "Yes", X_train_3["Fixed_Pred_Churn"], X_train_3["Pred_Churn"])

    report_precision_recall(
        y_train_3, X_train_3["Final_Churn_Pred"], "Fixed Training Metric"
    )


    X_test_2, y_test_2 = attach_pred_prob(
        X_test, y_test,
        "Pred_Churn", y_test_pred, 
        "Pred_Churn_Prod", y_test_pred_prob
    )

    y_test_2_pred = model2.predict(X_test_2)
    y_test_2_pred_prob = model2.predict_proba(X_test_2)[:, 1]

    X_test_3, y_test_3 = attach_pred_prob(
        X_test_2, y_test_2,
        "Fixed_Pred_Churn", y_test_2_pred, 
        "Fixed_Pred_Churn_Prod", y_test_2_pred_prob
    )
    X_test_3["Final_Churn_Pred"] = np.where(X_test_3["Pred_Churn"] == "Yes", X_test_3["Fixed_Pred_Churn"], X_test_3["Pred_Churn"])

    report_precision_recall(
        y_test_3, X_test_3["Final_Churn_Pred"], "Fixed Testing Metric"
    )

    plt.show()



    



   


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
