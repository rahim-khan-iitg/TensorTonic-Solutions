import math

def novelty_score(recommendations: list, item_counts: list, n_users: int) -> float:
    """
    Returns the average self-information of the recommended items.
    """
    # Write code here
    if len(recommendations)==0:
        return 0.0
    novelty=0.0
    for i in item_counts:
        prob=-math.log2(i / n_users) 
        novelty+=prob

    return novelty/len(item_counts)