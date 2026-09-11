import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import RadioButtons
from matplotlib.ticker import PercentFormatter
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils.multiclass import unique_labels


def report_precision_recall(true_value, pred_value, title="Classification Report"):
    """Render confusion-matrix counts, recall, and precision for predictions.

    Rows are actual classes and columns are predicted classes. Recall
    normalizes each actual-class row; precision normalizes each
    predicted-class column, retaining the same confusion-matrix orientation.

    ``title`` is shown above the complete report figure.
    """
    labels = unique_labels(true_value, pred_value)
    counts = confusion_matrix(true_value, pred_value, labels=labels)

    recall = np.divide(
        counts,
        counts.sum(axis=1, keepdims=True),
        out=np.zeros_like(counts, dtype=float),
        where=counts.sum(axis=1, keepdims=True) != 0,
    )
    precision = np.divide(
        counts,
        counts.sum(axis=0, keepdims=True),
        out=np.zeros_like(counts, dtype=float),
        where=counts.sum(axis=0, keepdims=True) != 0,
    )

    fig, ((table_ax, metrics_ax), (recall_ax, precision_ax)) = plt.subplots(
        2, 2, figsize=(16, 11)
    )
    fig.suptitle(f"{title} (Accuracy: {accuracy_score(true_value, pred_value):.3f})")

    table_ax.axis("off")
    table = table_ax.table(
        cellText=counts,
        rowLabels=[f"Actual {label}" for label in labels],
        colLabels=[f"Predicted {label}" for label in labels],
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.6)
    table_ax.set_title("Confusion Matrix: Raw Counts")

    metrics = classification_report(
        true_value,
        pred_value,
        labels=labels,
        target_names=[str(label) for label in labels],
        output_dict=True,
        zero_division=0,
    )
    metric_rows = [str(label) for label in labels] + ["macro avg", "weighted avg"]
    metric_table = [
        [
            f"{metrics[row]['precision']:.2f}",
            f"{metrics[row]['recall']:.2f}",
            f"{metrics[row]['f1-score']:.2f}",
            f"{metrics[row]['support']:.0f}",
        ]
        for row in metric_rows
    ]
    metrics_ax.axis("off")
    summary_table = metrics_ax.table(
        cellText=metric_table,
        rowLabels=metric_rows,
        colLabels=["Precision", "Recall", "F1 Score", "Support"],
        cellLoc="center",
        loc="center",
    )
    summary_table.auto_set_font_size(False)
    summary_table.set_fontsize(9)
    summary_table.scale(1.1, 1.6)
    metrics_ax.set_title("Classification Report")

    _plot_stacked_matrix(
        recall_ax, recall, labels, "actual", "predicted", "Recall by Actual Class"
    )
    _plot_stacked_matrix(
        precision_ax, precision, labels, "predicted", "actual", "Precision by Predicted Class"
    )

    fig.tight_layout(rect=(0, 0.03, 1, 0.95))
    return fig, ((table_ax, metrics_ax), (recall_ax, precision_ax))    


def _plot_stacked_matrix(ax, matrix, labels, bar_axis, segment_axis, title):
    """Draw a normalized confusion-matrix view using its matching axis."""
    positions = np.arange(len(labels))
    values_by_segment = matrix.T if bar_axis == "actual" else matrix

    if bar_axis == "actual":
        left = np.zeros(len(labels))
        for label, values in zip(labels, values_by_segment):
            ax.barh(positions, values, left=left, label=f"{segment_axis.title()}: {label}")
            for position, start, value in zip(positions, left, values):
                if value > 0:
                    ax.text(
                        start + value / 2,
                        position,
                        f"{value:.2%}",
                        ha="center",
                        va="center",
                        color="white" if value >= 0.12 else "black",
                        fontsize=9,
                    )
            left += values
        ax.set_yticks(positions, [str(label) for label in labels])
        ax.set_xlabel("Percentage")
        ax.set_ylabel("Actual Class")
        ax.set_xlim(0, 1)
        ax.xaxis.set_major_formatter(PercentFormatter(xmax=1))
        # Match confusion-matrix row order: the first actual class is on top.
        ax.invert_yaxis()
    else:
        bottom = np.zeros(len(labels))
        # Match confusion-matrix row order: the first actual class is on top.
        for label, values in zip(labels[::-1], values_by_segment[::-1]):
            ax.bar(positions, values, bottom=bottom, label=f"{segment_axis.title()}: {label}")
            for position, start, value in zip(positions, bottom, values):
                if value > 0:
                    ax.text(
                        position,
                        start + value / 2,
                        f"{value:.2%}",
                        ha="center",
                        va="center",
                        color="white" if value >= 0.12 else "black",
                        fontsize=9,
                    )
            bottom += values
        ax.set_xticks(positions, [str(label) for label in labels])
        ax.set_xlabel("Predicted Class")
        ax.set_ylabel("Percentage")
        ax.set_ylim(0, 1)
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))

    ax.set_title(title)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.35), ncol=2)


def _interactive_stacked_bar(counts, xlabel, hue_label, mode='count'):
    """Draw a stacked bar chart of a counts crosstab with a count/percent radio toggle."""
    if mode not in ('count', 'percent'):
        raise ValueError("mode must be 'count' or 'percent'")

    percents = counts.div(counts.sum(axis=1), axis=0) * 100
    data_by_mode = {'count': counts, 'percent': percents}

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.subplots_adjust(right=0.75, bottom=0.28)

    def draw(selected_mode):
        ax.clear()
        data_by_mode[selected_mode].plot(kind='bar', stacked=True, ax=ax, legend=False)
        ax.set_xlabel(xlabel)
        ax.set_ylabel('Percentage (%)' if selected_mode == 'percent' else 'Count')
        ax.set_title(f'{hue_label} by {xlabel}')
        ax.legend(title=hue_label, bbox_to_anchor=(1.02, 1), loc='upper left')
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        fig.canvas.draw_idle()

    draw(mode)

    radio_ax = fig.add_axes([0.4, 0.02, 0.2, 0.12])
    radio = RadioButtons(radio_ax, ('count', 'percent'), active=('count', 'percent').index(mode))
    radio.on_clicked(draw)
    # Keep a reference on the figure so the widget stays interactive after this function returns.
    fig._radio_buttons = radio

    return fig, ax


def plot_stacked_bar(df, category_column, hue_column, mode='count'):
    """Stacked bar chart of `hue_column` within each `category_column` category.

    Draws radio buttons on the figure so the user can toggle between raw
    counts and row-wise percentages after the plot is shown.
    """
    counts = pd.crosstab(df[category_column], df[hue_column])
    return _interactive_stacked_bar(counts, category_column, hue_column, mode)


def plot_binned_stacked_bar(df, numeric_column, hue_column, n_bins=10, mode='count'):
    """Stacked bar chart of `hue_column` across `n_bins` equal-width buckets of `numeric_column`.

    Draws radio buttons on the figure so the user can toggle between raw
    counts and row-wise percentages after the plot is shown.
    """
    bins = pd.cut(df[numeric_column], bins=n_bins)
    counts = pd.crosstab(bins, df[hue_column])
    counts.index = counts.index.astype(str)
    return _interactive_stacked_bar(counts, numeric_column, hue_column, mode)


def _interactive_heatmap(data_by_mode, xlabel, ylabel, mode='count', title=None):
    """Draw a 2D heatmap from precomputed {'count': df, 'percent': df} data with a radio toggle."""
    if mode not in ('count', 'percent'):
        raise ValueError("mode must be 'count' or 'percent'")

    title = title or f'{ylabel} vs {xlabel}'

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.subplots_adjust(bottom=0.3)
    state = {'cbar': None}

    def draw(selected_mode):
        if state['cbar'] is not None:
            state['cbar'].remove()
            state['cbar'] = None
        ax.clear()

        data = data_by_mode[selected_mode]
        im = ax.imshow(data.values, cmap='viridis', aspect='auto', origin='lower')
        ax.set_xticks(range(len(data.columns)))
        ax.set_xticklabels(data.columns.astype(str), rotation=45, ha='right')
        ax.set_yticks(range(len(data.index)))
        ax.set_yticklabels(data.index.astype(str))
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        vmax = data.values.max()
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                val = data.values[i, j]
                text = f'{val:.1f}%' if selected_mode == 'percent' else f'{val:g}'
                color = 'white' if vmax and val < vmax / 2 else 'black'
                ax.text(j, i, text, ha='center', va='center', color=color, fontsize=8)

        state['cbar'] = fig.colorbar(im, ax=ax, label='Percentage (%)' if selected_mode == 'percent' else 'Count')
        fig.canvas.draw_idle()

    draw(mode)

    radio_ax = fig.add_axes([0.4, 0.02, 0.2, 0.12])
    radio = RadioButtons(radio_ax, ('count', 'percent'), active=('count', 'percent').index(mode))
    radio.on_clicked(draw)
    # Keep a reference on the figure so the widget stays interactive after this function returns.
    fig._radio_buttons = radio

    return fig, ax


def plot_2d_binned_heatmap(df, x_column, y_column, n_bins=10, mode='count'):
    """2D heatmap of row counts across `n_bins` buckets of `x_column` and `y_column`.

    Each cell shows the number of rows falling into that (x, y) bucket pair, or
    that count as a percentage of all rows. Draws radio buttons on the figure
    so the user can toggle between the two after the plot is shown.
    """
    x_bins = pd.cut(df[x_column], bins=n_bins)
    y_bins = pd.cut(df[y_column], bins=n_bins)
    counts = pd.crosstab(y_bins, x_bins)
    percents = counts / counts.values.sum() * 100
    counts.index = percents.index = counts.index.astype(str)
    counts.columns = percents.columns = counts.columns.astype(str)
    data_by_mode = {'count': counts, 'percent': percents}
    return _interactive_heatmap(data_by_mode, x_column, y_column, mode)


def plot_2d_binned_heatmap_by_category(df, x_column, y_column, category_column, category_value, n_bins=10, mode='count'):
    """2D heatmap of `category_value` occurrences across `n_bins` buckets of `x_column` and `y_column`.

    Each cell shows either the count of rows where `category_column == category_value`
    within that (x, y) bucket, or that count as a percentage of all rows (any category)
    falling into the same bucket. Draws radio buttons on the figure so the user can
    toggle between the two after the plot is shown.
    """
    x_bins = pd.cut(df[x_column], bins=n_bins)
    y_bins = pd.cut(df[y_column], bins=n_bins)

    total_counts = pd.crosstab(y_bins, x_bins)
    is_category = df[category_column] == category_value
    category_counts = pd.crosstab(y_bins[is_category], x_bins[is_category])
    category_counts = category_counts.reindex(index=total_counts.index, columns=total_counts.columns, fill_value=0)

    percents = (category_counts / total_counts.replace(0, np.nan) * 100).fillna(0)
    category_counts.index = percents.index = category_counts.index.astype(str)
    category_counts.columns = percents.columns = category_counts.columns.astype(str)
    data_by_mode = {'count': category_counts, 'percent': percents}

    title = f'{category_column} = {category_value}'
    return _interactive_heatmap(data_by_mode, x_column, y_column, mode, title=title)


def plot_scatter_by_category(df, x_column, y_column, category_column):
    """Scatter plot of `x_column` vs `y_column`, colored by `category_column`."""
    fig, ax = plt.subplots(figsize=(8, 6))

    categories = df[category_column].unique()
    cmap = plt.get_cmap('tab10' if len(categories) <= 10 else 'tab20')

    for i, category in enumerate(categories):
        subset = df[df[category_column] == category]
        ax.scatter(subset[x_column], subset[y_column], color=cmap(i), label=str(category), alpha=0.7)

    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'{y_column} vs {x_column} by {category_column}')
    ax.legend(title=category_column, bbox_to_anchor=(1.02, 1), loc='upper left')
    fig.tight_layout()

    return fig, ax
