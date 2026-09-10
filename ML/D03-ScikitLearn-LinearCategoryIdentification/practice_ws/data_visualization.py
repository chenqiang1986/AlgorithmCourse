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
        errors='coerce').fillna(0)

    df['ChargeRatio'] = df['TotalCharges'] / df['tenure']
    
    target_column = ['Churn']

    numeric_columns = [
        'tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen', 'ChargeRatio'
    ]

    category_columns = [
        'gender', 
        'Partner',
        'Dependents',
        'PhoneService', 'MultipleLines', # Phone service is redudant

        'InternetService',
        # No need to include No Internet Service for the following features.
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 

       'Contract', 
       'PaperlessBilling', 'PaymentMethod',
    ]

    feature_columns = numeric_columns + category_columns

    X = df[feature_columns]
    y = df[target_column[0]]

    plot_stacked_bar(df, 'SeniorCitizen', 'Churn')
    #plot_binned_stacked_bar(df[df['InternetService'] == 'Fiber optic'], 'Contract', 'Churn', n_bins=20)
    #plot_binned_stacked_bar(df[df['InternetService'] == 'DSL'], 'Contract', 'Churn', n_bins=20)
    #plot_binned_stacked_bar(df[df['InternetService'] == 'No'], 'Contract', 'Churn', n_bins=20)

    plot_stacked_bar(df[df['Contract'] == 'Two year'], 'tenure', 'Churn')
    plot_stacked_bar(df[df['Contract'] == 'One year'], 'tenure', 'Churn')
    plot_stacked_bar(df[df['Contract'] == 'Month-to-month'], 'tenure', 'Churn')
    plt.show()

if __name__ == "__main__":
    main()
