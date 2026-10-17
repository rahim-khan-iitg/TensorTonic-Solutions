def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    recommended=set(recommended[:k])
    relevant=set(relevant)
    intersection=recommended.intersection(relevant)
    precion=len(intersection)/k
    recall=len(intersection)/len(relevant)
    return [precion,recall]