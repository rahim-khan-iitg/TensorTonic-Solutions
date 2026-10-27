import math

def binary_focal_loss(predictions: list, targets: list, alpha: float, gamma: float) -> float:
    """
    Returns the mean binary focal loss as a float.
    """
    # Write code here
    loss=[]
    for i in range(len(predictions)):
        if targets[i]==1:
            pt=predictions[i]
        else:
            pt=1-predictions[i]
        fl=-alpha*math.log(pt)*(1-pt)**gamma
        loss.append(fl)
    return sum(loss)/len(loss)