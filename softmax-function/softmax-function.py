import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    arr=np.array(x)
    shape=arr.shape
    row_max=arr.max(axis=-1).reshape(-1,1)
    arr=arr-row_max
    exps=np.exp(arr)
    row_sum=np.sum(exps,axis=-1).reshape(-1,1)
    softmx=exps/row_sum
    softmx=softmx.reshape(shape)
    return softmx