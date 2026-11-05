def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    # Write code here
    ans=[]
    for value in values:
        powers=[1]
        for i in range(1,degree+1):
            powers.append(value**i)
        ans.append(powers)
    return ans