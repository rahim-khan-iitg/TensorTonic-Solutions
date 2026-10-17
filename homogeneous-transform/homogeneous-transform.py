import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    T=np.array(T)
    if isinstance(points[0],int):
      points.append(1)
    elif isinstance(points[0],list):
      for point in points:
        point.append(1)
    points=np.array(points).reshape(-1,4)
    print(T.shape)
    print(points.shape)
    ph=T@points.T
    return ph.T[:,:3].squeeze()