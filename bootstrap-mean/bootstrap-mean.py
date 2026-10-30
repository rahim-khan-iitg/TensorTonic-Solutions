import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)

    x = np.asarray(x)
    x_size = len(x)

    b_vals = []

    for _ in range(n_bootstrap):
        sample = rng.choice(x, size=x_size, replace=True)
        b_vals.append(sample.mean().item())

    b_vals = np.array(b_vals)

    bootstrap_mean = b_vals.mean().item()

    alpha = (1 - ci) / 2

    lower = np.quantile(b_vals, alpha).item()
    upper = np.quantile(b_vals, 1 - alpha).item()

    return {
        "bootstrap_mean": bootstrap_mean,
        "lower": lower,
        "upper": upper
    }