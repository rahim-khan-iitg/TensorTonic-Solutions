import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    u=np.array(w)
    v=np.array(v)
    dot_prod=np.dot(u,v)
    norm_u=np.linalg.norm(u,2)
    norm_v=np.linalg.norm(v,2)
    c=dot_prod/(norm_u*norm_v)
    c=np.clip(c,-1,1)
    return np.acos(c).item()