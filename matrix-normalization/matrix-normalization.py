
import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    matrix = np.array(matrix, dtype=np.float64)

    if norm_type not in ("l1", "l2", "max"):
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")

    if axis not in (None, 0, 1):
        raise ValueError("axis must be None, 0, or 1")

    if norm_type == "l1":
        norm = np.sum(np.abs(matrix), axis=axis)
    elif norm_type == "l2":
        norm = np.sqrt(np.sum(matrix ** 2, axis=axis))
    else:
        norm = np.max(np.abs(matrix), axis=axis)

    if axis is not None:
        norm = np.expand_dims(norm, axis=axis)

    norm = np.where(norm == 0, 1.0, norm)

    return matrix / norm