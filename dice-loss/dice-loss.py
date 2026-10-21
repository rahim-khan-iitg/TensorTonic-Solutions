import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p=np.array(p)
    y=np.array(y)
    num=(2*y*p).sum() +eps
    denom=p.sum()+y.sum()+eps
    return (1-num/denom).item()
