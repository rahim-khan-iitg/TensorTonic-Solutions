import math
def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    # Write code here
    sum_w=sum(weights)
    ans=[]
    length=len(weights)
    for i in range(len(values)-length+1):
      vals=values[i:i+length]
      s=0
      for i in range(length):
        s+=vals[i]*weights[i]
      ans.append(s/sum_w)
    return ans