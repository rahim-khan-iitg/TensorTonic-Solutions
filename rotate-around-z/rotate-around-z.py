import numpy as np
import math
def rotate_around_z(points: list, theta: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as points.
    """
    X=np.array(points)
    shape=X.shape
    # X=X.reshape(3,-1)
    mat=np.array([[math.cos(theta),math.sin(-theta),0],[math.sin(theta),math.cos(theta),0],[0,0,1]])
    res=mat@X.T
    return res.T
