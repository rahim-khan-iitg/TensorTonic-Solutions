def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    ans=series
    diff=[]
    for d in range(order):
        for i in range(1,len(ans)):
            diff.append(ans[i]-ans[i-1])
        ans=diff
        diff=[]
    return ans
    