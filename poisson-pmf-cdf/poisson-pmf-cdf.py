import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    x_lte_k=[]
    for i in range(k+1):
        term=math.exp(-lam)*math.pow(lam,i)/math.factorial(i)
        x_lte_k.append(term)
    pmf=x_lte_k[-1]
    cdf=sum(x_lte_k)
    return {"pmf":pmf,"cdf":cdf}