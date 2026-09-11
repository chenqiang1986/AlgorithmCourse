"""Helpers for visualizing binary-classification ROC curves."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import auc, roc_curve


def plot_roc(probabilities, actual_values, positive_label=1, ax=None):
    """Plot a ROC curve from positive-class probabilities and true labels.

    Parameters
    ----------
    probabilities : array-like of shape (n_samples,)
        Predicted probabilities (or any continuous scores) for the positive
        class.
    actual_values : array-like of shape (n_samples,)
        True binary labels. Values equal to ``positive_label`` are treated as
        the positive class.
    positive_label : object, default=1
        Label that identifies the positive class in ``actual_values``.
    ax : matplotlib.axes.Axes, optional
        Existing axes on which to draw. A new figure and axes are created when
        omitted.

    Returns
    -------
    Examples
    --------
    >>> probabilities = [0.05, 0.80, 0.35, 0.90]
    >>> actual_values = [0, 1, 0, 1]
    >>> plot_roc(probabilities, actual_values)
    """
    probabilities = np.asarray(probabilities).reshape(-1)
    actual_values = np.asarray(actual_values).reshape(-1)

    if probabilities.size == 0:
        raise ValueError("probabilities and actual_values must not be empty")
    if probabilities.size != actual_values.size:
        raise ValueError("probabilities and actual_values must have the same length")
    if not np.issubdtype(probabilities.dtype, np.number):
        raise ValueError("probabilities must contain numeric scores")
    if not np.isfinite(probabilities).all():
        raise ValueError("probabilities must not contain NaN or infinite values")

    binary_actuals = actual_values == positive_label
    if binary_actuals.all() or (~binary_actuals).all():
        raise ValueError("actual_values must contain both positive and negative classes")

    false_positive_rate, true_positive_rate, _ = roc_curve(
        actual_values, probabilities, pos_label=positive_label
    )
    roc_auc = auc(false_positive_rate, true_positive_rate)

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 6))
    else:
        fig = ax.figure

    ax.plot(
        false_positive_rate,
        true_positive_rate,
        linewidth=2,
        label=f"ROC curve (AUC = {roc_auc:.3f})",
    )
    ax.plot([0, 1], [0, 1], "--", color="gray", label="Random classifier")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Receiver Operating Characteristic (ROC) Curve")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(loc="lower right")
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()
    plt.show()
