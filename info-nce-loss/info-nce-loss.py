import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    z1=np.array(Z1)
    z2=np.array(Z2)
    S=z1@z2.T/temperature
    ans=0;
    N=len(Z1)
    for i in range(N):
        row_max=S[i,:].max()
        numerator=np.exp(S[i,i]-row_max)
        denominator=np.sum(np.exp(S[i,:]-row_max))
        ans+=np.log(numerator/denominator)
    return (-ans/N).item()