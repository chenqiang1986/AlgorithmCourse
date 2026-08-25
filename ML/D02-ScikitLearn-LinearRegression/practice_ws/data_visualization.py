import pandas as pd
import matplotlib.pyplot as plt


def plot_sales_by_store(df, col_name, n_cols=7):
    # Sum Weekly_Sales per store per year, collapsing all other features (month, holiday, etc.)
    yearly_sales = df.groupby(["Store", col_name])["Weekly_Sales"].mean().reset_index()

    stores = sorted(yearly_sales["Store"].unique())
    n_rows = -(-len(stores) // n_cols)  # ceil division

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 3, n_rows * 2.5), sharex=True)
    axes = axes.flatten()

    for ax, store in zip(axes, stores):
        store_data = yearly_sales[yearly_sales["Store"] == store]
        ax.plot(store_data[col_name], store_data["Weekly_Sales"], marker="o", color="#2f6fed")
        ax.set_title(f"Store {store}", fontsize=9)
        ax.tick_params(labelsize=7, labelbottom=True)

    for ax in axes[len(stores):]:
        ax.axis("off")

    fig.suptitle(f"{col_name} Total Weekly Sales by Store")
    fig.supxlabel(col_name)
    fig.supylabel("Weekly Sales")
    fig.tight_layout()
    plt.show()


def main():
    df = pd.read_csv("Walmart_Sales.csv")

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    print(df.head())

    plot_sales_by_store(df, "Holiday_Flag")


if __name__=="__main__":
    main()