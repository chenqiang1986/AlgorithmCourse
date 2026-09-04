import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import CheckButtons, Slider
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def mean_abs_p_error(actual, pred):
    diff = actual - pred
    diff = diff.abs()
    diff = diff / actual
    return diff.mean()


df = pd.read_csv("Walmart_Sales.csv")

# Step 1: convert raw dates
df["dates"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')

# Step 2: create date features
df["month"] = df["dates"].dt.month
df["dayofweek"] = df["dates"].dt.dayofweek
df["year"] = df["dates"].dt.year
df["doy"]= df["dates"].dt.day_of_year

# Step 3: choose features and target
X = df[[
    "Store",
    "Holiday_Flag",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "month",
    "doy",
    "year",
    "Unemployment"
]]
y = df["Weekly_Sales"]

# Step 4: plot average Weekly_Sales against each X feature, with a toggle to
# view all stores at once or isolate a single store via a slider
stores = sorted(df["Store"].unique())
colors = plt.cm.viridis(np.linspace(0, 1, len(stores)))
store_color = dict(zip(stores, colors))

fig, axes = plt.subplots(3, 3, figsize=(15, 13))
fig.subplots_adjust(left=0.06, right=0.92, top=0.95, bottom=0.16, hspace=0.45, wspace=0.3)
axes_flat = axes.flatten()

lines_by_feature = {}
store_ax = None
store_scatter = None

for feature, ax in zip(X.columns, axes_flat):
    ax.set_xlabel(feature)
    ax.set_ylabel("Average Weekly_Sales")
    ax.set_title(f"Weekly_Sales vs {feature}")

    if feature == "Store":
        store_ax = ax
        avg_by_feature = df.groupby(feature)["Weekly_Sales"].mean()
        store_scatter = ax.scatter(
            avg_by_feature.index,
            avg_by_feature.values,
            s=30,
            c=[store_color[s] for s in avg_by_feature.index],
        )
    else:
        avg_by_feature_store = df.groupby([feature, "Store"])["Weekly_Sales"].mean()
        lines_by_feature[feature] = {}
        for store in stores:
            series = avg_by_feature_store.xs(store, level="Store").sort_index()
            line, = ax.plot(series.index, series.values, color=store_color[store], linewidth=0.8, alpha=0.7)
            lines_by_feature[feature][store] = line

sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(vmin=min(stores), vmax=max(stores)))
fig.colorbar(sm, ax=axes, label="Store", shrink=0.6)

# widgets: checkbox to show every store at once, slider to isolate one store
check_ax = fig.add_axes((0.06, 0.02, 0.15, 0.06))
show_all_check = CheckButtons(check_ax, ["Show all stores"], [True])

slider_ax = fig.add_axes((0.3, 0.045, 0.5, 0.02))
store_slider = Slider(slider_ax, "Store", min(stores), max(stores), valinit=stores[0], valstep=stores)


def update(_event=None):
    show_all = show_all_check.get_status()[0]
    selected_store = int(store_slider.val)

    for feature, store_lines in lines_by_feature.items():
        ax = axes_flat[list(X.columns).index(feature)]
        for store, line in store_lines.items():
            if show_all:
                line.set_visible(True)
                line.set_alpha(0.7)
                line.set_linewidth(0.8)
            else:
                line.set_visible(store == selected_store)
                line.set_alpha(1.0)
                line.set_linewidth(1.5)
        if show_all:
            ax.relim()
            ax.autoscale()
        else:
            selected_line = store_lines[selected_store]
            xs, ys = selected_line.get_xdata(), selected_line.get_ydata()
            ax.set_xlim(min(xs), max(xs))
            pad = (max(ys) - min(ys)) * 0.1 or 1
            ax.set_ylim(min(ys) - pad, max(ys) + pad)

    sizes = [80 if (not show_all and s == selected_store) else 30 for s in stores]
    edge_colors = ["black" if (not show_all and s == selected_store) else "none" for s in stores]
    store_scatter.set_sizes(sizes)
    store_scatter.set_edgecolors(edge_colors)

    fig.canvas.draw_idle()


show_all_check.on_clicked(update)
store_slider.on_changed(update)

update()
plt.show()
