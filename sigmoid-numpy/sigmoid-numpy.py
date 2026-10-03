import numpy as np
import math
def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    if isinstance(x,list):
        x=np.array(x)
        sigma_x=1/(1+np.exp(-x))
        return sigma_x
    else:
        return 1/(1+math.exp(-x))