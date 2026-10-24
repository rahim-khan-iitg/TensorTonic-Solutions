import numpy as np
def lbfgs_direction(grad: list, s_list: list, y_list: list) -> list:
    """
    Returns the L-BFGS descent direction from the stored history.
    """
    grad=np.array(grad)
    s_list=np.array(s_list)
    y_list=np.array(y_list)
    rho=[]
    alphas=[]
    for i in range(len(s_list)):
        val=(1/np.dot(s_list[i],y_list[i]).item())
        rho.append(val)
    for i in range(len(rho)-1,-1,-1):
        alpha=rho[i]*np.dot(s_list[i],grad).item()
        alphas.insert(0,alpha)
        grad=grad-alpha*y_list[i]
    gamma=(np.dot(s_list[-1],y_list[-1])/np.dot(y_list[-1],y_list[-1])).item()
    r=gamma*grad
    for i in range(len(rho)):
        beta=rho[i]*np.dot(y_list[i],r).item()
        r=r+s_list[i]*(alphas[i]-beta)
    r=-1*r
    return r.tolist()
