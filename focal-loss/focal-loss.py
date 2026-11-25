import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    p=np.array(p)
    y=np.array(y)
    l=-((1-p)**gamma)*y*np.log(p)-(p**gamma)*(1-y)*np.log(1-p)
    return l.mean().item()