import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)
    xtx=X.T@X
    xtx_in=np.linalg.inv(xtx)
    ans=xtx_in@X.T@y
    return ans