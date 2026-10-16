import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    A=np.array([list(range(d_model))]*seq_len,dtype=np.float64)
    even=base**((A[:,::2])/d_model)
    odd=base**((A[:,1::2]-1)/d_model)
    pos=np.array(list(range(seq_len)),dtype=np.float64)
    even=pos.reshape(-1,1)/even
    odd=pos.reshape(-1,1)/odd
    even=np.sin(even)
    odd=np.cos(odd)
    A[:,::2]=even
    A[:,1::2]=odd
    return A