
def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    # Write code here
    n=len(values)
    freqs=dict()
    for i in range(n):
        if values[i] not in freqs:
            freqs[values[i]]=1
        else:
            freqs[values[i]]+=1
    ans=[]
    for i in range(n):
        enc=freqs[values[i]]/n
        ans.append(enc)
    return ans