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
