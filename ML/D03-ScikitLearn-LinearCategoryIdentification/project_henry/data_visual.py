import pandas as pd
from plot_graphs import plot_stacked_bar, plot_binned_stacked_bar
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df["TotalCharges"] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df["TotalCharges"] = df["TotalCharges"].fillna(0)

print(df["PaymentMethod"].unique())

plot_stacked_bar(df=df, category_column="PaymentMethod", hue_column="Churn")
plot_binned_stacked_bar(df=df[df["PaymentMethod"] == 'Electronic check'], numeric_column="MonthlyCharges", hue_column="Churn")
plot_binned_stacked_bar(df=df[df["PaymentMethod"] == 'Mailed check'], numeric_column="MonthlyCharges", hue_column="Churn")
plot_binned_stacked_bar(df=df[df["PaymentMethod"] == 'Bank transfer (automatic)'], numeric_column="MonthlyCharges", hue_column="Churn")
plot_binned_stacked_bar(df=df[df["PaymentMethod"] == 'Credit card (automatic)'], numeric_column="MonthlyCharges", hue_column="Churn")
#plot_binned_stacked_bar(df=df, numeric_column="TotalCharges", hue_column="Churn", n_bins=20)


# seniors, more churn
# has partner, less churn
# has dependents, less churn
# internet connection, more churn
# has internet safety, less churn
# longer tenure, longer contract, less churn
# paperless billing, more churn
# electronic check, more churn
# more total charge, less churn

plt.show()