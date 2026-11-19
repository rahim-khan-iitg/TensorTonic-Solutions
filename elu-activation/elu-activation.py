import math
def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    ans=[]
    for element in x:
        if element>0:
            ans.append(element)
        else:
            ans.append(alpha*(math.exp(element)-1))
    return ans