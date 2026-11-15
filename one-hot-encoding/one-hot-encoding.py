import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    k=max(y)+1
    if num_classes is not None:
        k=num_classes
    ans=[[0]*k for _ in range(len(y))]
    for i,c in enumerate(y):
        ans[i][c]=1

    return np.array(ans)
        