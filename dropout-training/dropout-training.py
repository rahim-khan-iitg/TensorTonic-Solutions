import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    x=np.array(x)
    probs=None
    if rng is not None:
      probs=rng.random(x.shape)
    else:
      probs=np.random.random(x.shape)
    mask=probs>=p
    probs=1/(1-p)*np.ones_like(x)
    zeros=np.zeros_like(probs)
    drop=np.where(mask,probs,zeros)
    return (x*drop,drop)