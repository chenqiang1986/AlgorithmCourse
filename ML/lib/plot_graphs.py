import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import RadioButtons


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
    x_bins = pd.cut(df[x_column], bins=n_bins).astype(str)
    y_bins = pd.cut(df[y_column], bins=n_bins).astype(str)
    counts = pd.crosstab(y_bins, x_bins)
    percents = counts / counts.values.sum() * 100
    data_by_mode = {'count': counts, 'percent': percents}
    return _interactive_heatmap(data_by_mode, x_column, y_column, mode)


def plot_2d_binned_heatmap_by_category(df, x_column, y_column, category_column, category_value, n_bins=10, mode='count'):
    """2D heatmap of `category_value` occurrences across `n_bins` buckets of `x_column` and `y_column`.

    Each cell shows either the count of rows where `category_column == category_value`
    within that (x, y) bucket, or that count as a percentage of all rows (any category)
    falling into the same bucket. Draws radio buttons on the figure so the user can
    toggle between the two after the plot is shown.
    """
    x_bins = pd.cut(df[x_column], bins=n_bins).astype(str)
    y_bins = pd.cut(df[y_column], bins=n_bins).astype(str)

    total_counts = pd.crosstab(y_bins, x_bins)
    is_category = df[category_column] == category_value
    category_counts = pd.crosstab(y_bins[is_category], x_bins[is_category])
    category_counts = category_counts.reindex(index=total_counts.index, columns=total_counts.columns, fill_value=0)

    percents = (category_counts / total_counts.replace(0, pd.NA) * 100).fillna(0)
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
