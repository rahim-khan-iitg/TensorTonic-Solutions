import math

def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    # Write code here
    if max(values)==min(values):
        return [0]*len(values)
    w=(max(values)-min(values))/num_bins
    bins=[]
    min_val=min(values)
    for val in values:
        bin=min(math.floor((val-min_val)/w),num_bins-1)
        bins.append(bin)
    return bins