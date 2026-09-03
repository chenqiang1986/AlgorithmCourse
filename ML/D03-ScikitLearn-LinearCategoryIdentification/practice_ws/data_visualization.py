import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from plot_graphs import plot_stacked_bar, plot_binned_stacked_bar

def main():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'], 
        errors='coerce').fillna(1)

    df['ChargeRatio'] = (np.log1p(df['MonthlyCharges'] * df['tenure']) - np.log1p(df['TotalCharges']))
    
    target_column = ['Churn']

    numeric_columns = [
        'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen', 'ChargeRatio'
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

    plot_stacked_bar(df, 'InternetService', 'Churn')
    plot_binned_stacked_bar(df[df['InternetService'] == 'Fiber optic'], 'MonthlyCharges', 'Churn', n_bins=20)
    plot_binned_stacked_bar(df[df['InternetService'] == 'DSL'], 'MonthlyCharges', 'Churn', n_bins=20)
    plot_binned_stacked_bar(df[df['InternetService'] == 'No'], 'MonthlyCharges', 'Churn', n_bins=20)
    plt.show()

if __name__ == "__main__":
    main()
