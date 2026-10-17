import numpy as np
import math
from collections import Counter
def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    counts=Counter(y)
    s=sum(counts.values())
    entropy=0.0
    for v in counts.values():
        entropy+=-(v/s)*math.log2(v/s)
    return entropy
