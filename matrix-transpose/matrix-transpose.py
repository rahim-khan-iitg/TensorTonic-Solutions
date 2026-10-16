import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
  """
  Returns the transposed matrix as a NumPy array.
  """
  arr=np.array(A)
  return arr.T
