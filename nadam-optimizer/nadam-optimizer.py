import numpy as np

def nadam_step(w: list, m: list, v: list, grad: list, lr: float = 0.002, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w, new_m, and new_v.
    """
    # Write code here
    w=np.array(w,dtype=np.float64)
    m=np.array(m,dtype=np.float64)
    v=np.array(v,dtype=np.float64)
    grad=np.array(grad,dtype=np.float64)
    mt=beta1*m+(1-beta1)*grad
    vt=beta2*v+(1-beta2)*grad*grad
    m_adjusted=beta1*mt+(1-beta1)*grad
    wt=w-lr*m_adjusted/(np.sqrt(vt)+eps)
    return  {"new_w": wt, "new_m": mt, "new_v": vt}