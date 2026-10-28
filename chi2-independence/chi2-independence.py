import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    observed = np.array(C, dtype=float)

    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    grand_total = observed.sum()

    expected = (row_totals @ col_totals) / grand_total

    chi2 = np.sum((observed - expected) ** 2 / expected)

    return {
        "chi2": float(chi2),
        "expected": expected
    }