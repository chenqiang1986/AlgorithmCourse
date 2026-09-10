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
from plot_graphs import plot_stacked_bar, plot_binned_stacked_bar, plot_scatter_by_category, plot_2d_binned_heatmap_by_category

def main():
    df = pd.read_csv("Remainder_for_Model2.csv")
    print(df.columns)
 

    #plot_stacked_bar(df, 'Contract', 'Churn')
    #plot_binned_stacked_bar(df, 'MonthlyCharges', 'Churn', n_bins=20)
    #plot_stacked_bar(df, "TechSupport", "Churn")

    #plot_binned_stacked_bar(df[df['InternetService'] == 'Fiber optic'], 'Contract', 'Churn', n_bins=20)
    #plot_binned_stacked_bar(df[df['InternetService'] == 'DSL'], 'Contract', 'Churn', n_bins=20)
    #plot_binned_stacked_bar(df[df['InternetService'] == 'No'], 'Contract', 'Churn', n_bins=20)

    #plot_binned_stacked_bar(df[df['Contract'] == 'Two year'], 'tenure', 'Churn')
    #plot_binned_stacked_bar(df[df['Contract'] == 'One year'], 'tenure', 'Churn')
    #plot_binned_stacked_bar(df[df['Contract'] == 'Month-to-month'], 'tenure', 'Churn')

    #plot_binned_stacked_bar(df, 'Pred_Churn_Prod', 'Churn')
    plot_2d_binned_heatmap_by_category(df, "tenure", "Pred_Churn_Prod", "Churn", "No")
    plt.show()

if __name__ == "__main__":
    main()
