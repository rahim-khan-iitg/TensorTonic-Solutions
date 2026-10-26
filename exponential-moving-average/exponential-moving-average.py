def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here
    ans=[values[0]]
    for i in range(1,len(values)):
        ema=alpha*values[i]+(1-alpha)*ans[-1]
        ans.append(ema)
    return ans