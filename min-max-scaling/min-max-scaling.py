import numpy as np
def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Write code here
    arr=np.array(data,dtype=float)
    col_max=np.max(arr,axis=0)
    col_min=np.min(arr,axis=0)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if col_max[j]==col_min[j]:
                arr[i][j]=0.0
            else:
                arr[i][j]=(arr[i][j]-col_min[j])/(col_max[j]-col_min[j])
    return arr.tolist()