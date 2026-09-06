import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import CheckButtons, RangeSlider, Slider
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

HIST_FEATURES = {"Temperature", "Fuel_Price", "CPI", "Unemployment"}
HIST_BINS = 15

fig, axes = plt.subplots(3, 3, figsize=(15, 13))
fig.subplots_adjust(left=0.06, right=0.92, top=0.95, bottom=0.24, hspace=0.45, wspace=0.3)
axes_flat = axes.flatten()

lines_by_feature = {}
hist_axes = {}
store_ax = None
store_scatter = None


def draw_histogram(ax, feature, feature_values, sales_values):
    ax.cla()
    ax.set_xlabel(feature)
    ax.set_ylabel("Average Weekly_Sales")
    ax.set_title(f"Weekly_Sales vs {feature}")

    if feature_values.empty:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        return

    bins = pd.cut(feature_values, bins=HIST_BINS)
    avg_sales_by_bin = sales_values.groupby(bins, observed=True).mean()
    centers = [interval.mid for interval in avg_sales_by_bin.index]
    width = (feature_values.max() - feature_values.min()) / HIST_BINS
    ax.bar(centers, avg_sales_by_bin.values, width=width * 0.9, color="steelblue", edgecolor="white")


for feature, ax in zip(X.columns, axes_flat):
    ax.set_xlabel(feature)
    ax.set_ylabel("Average Weekly_Sales")
    ax.set_title(f"Weekly_Sales vs {feature}")

    if feature == "Store":
        store_ax = ax
        store_scatter = ax.scatter([], [], s=30)
    elif feature in HIST_FEATURES:
        hist_axes[feature] = ax
    else:
        lines_by_feature[feature] = {}
        for store in stores:
            line, = ax.plot([], [], color=store_color[store], linewidth=0.8, alpha=0.7)
            lines_by_feature[feature][store] = line

sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(vmin=min(stores), vmax=max(stores)))
fig.colorbar(sm, ax=axes, label="Store", shrink=0.6)

# widgets: checkbox to show every store at once, slider to isolate one store,
# and a range slider to restrict the date period used everywhere above
check_ax = fig.add_axes((0.06, 0.03, 0.15, 0.06))
show_all_check = CheckButtons(check_ax, ["Show all stores"], [True])

slider_ax = fig.add_axes((0.3, 0.145, 0.5, 0.02))
store_slider = Slider(slider_ax, "Store", min(stores), max(stores), valinit=stores[0], valstep=stores)

date_min_num = mdates.date2num(df["dates"].min())
date_max_num = mdates.date2num(df["dates"].max())
time_slider_ax = fig.add_axes((0.3, 0.08, 0.5, 0.02))
time_slider = RangeSlider(time_slider_ax, "Date range", date_min_num, date_max_num, valinit=(date_min_num, date_max_num))
time_slider.valtext.set_visible(False)


def update(_event=None):
    show_all = show_all_check.get_status()[0]
    selected_store = int(store_slider.val)

    date_lo_num, date_hi_num = time_slider.val
    date_lo = pd.Timestamp(mdates.num2date(date_lo_num)).tz_localize(None)
    date_hi = pd.Timestamp(mdates.num2date(date_hi_num)).tz_localize(None)
    time_slider_ax.set_title(f"{date_lo.date()} to {date_hi.date()}", fontsize=9)
    date_filtered = df[(df["dates"] >= date_lo) & (df["dates"] <= date_hi)]

    avg_by_store = date_filtered.groupby("Store")["Weekly_Sales"].mean().reindex(stores)
    store_scatter.set_offsets(np.column_stack([avg_by_store.index, avg_by_store.values]))
    store_scatter.set_color([store_color[s] for s in avg_by_store.index])
    valid_stores = avg_by_store.dropna()
    if len(valid_stores):
        xs, ys = valid_stores.index.values, valid_stores.values
        x_pad = (max(xs) - min(xs)) * 0.05 or 1
        y_pad = (max(ys) - min(ys)) * 0.1 or 1
        store_ax.set_xlim(min(xs) - x_pad, max(xs) + x_pad)
        store_ax.set_ylim(min(ys) - y_pad, max(ys) + y_pad)

    for feature, store_lines in lines_by_feature.items():
        ax = axes_flat[list(X.columns).index(feature)]
        avg_by_feature_store = date_filtered.groupby([feature, "Store"])["Weekly_Sales"].mean()
        present_stores = set(avg_by_feature_store.index.get_level_values("Store"))
        for store, line in store_lines.items():
            if store in present_stores:
                series = avg_by_feature_store.xs(store, level="Store").sort_index()
                line.set_data(series.index.values, series.values)
            else:
                line.set_data([], [])
            has_data = store in present_stores
            if show_all:
                line.set_visible(has_data)
                line.set_alpha(0.7)
                line.set_linewidth(0.8)
            else:
                line.set_visible(has_data and store == selected_store)
                line.set_alpha(1.0)
                line.set_linewidth(1.5)
        if show_all:
            ax.relim()
            ax.autoscale()
        else:
            selected_line = store_lines[selected_store]
            xs, ys = selected_line.get_xdata(), selected_line.get_ydata()
            if len(xs):
                ax.set_xlim(min(xs), max(xs))
                pad = (max(ys) - min(ys)) * 0.1 or 1
                ax.set_ylim(min(ys) - pad, max(ys) + pad)

    for feature, ax in hist_axes.items():
        rows = date_filtered if show_all else date_filtered.loc[date_filtered["Store"] == selected_store]
        draw_histogram(ax, feature, rows[feature], rows["Weekly_Sales"])

    sizes = [80 if (not show_all and s == selected_store) else 30 for s in avg_by_store.index]
    edge_colors = ["black" if (not show_all and s == selected_store) else "none" for s in avg_by_store.index]
    store_scatter.set_sizes(sizes)
    store_scatter.set_edgecolors(edge_colors)

    fig.canvas.draw_idle()


show_all_check.on_clicked(update)
store_slider.on_changed(update)
time_slider.on_changed(update)

update()
plt.show()
