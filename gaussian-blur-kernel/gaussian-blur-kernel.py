import math
def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    coords=[-i for i in range(size//2,0,-1)]+[i for i in range(0,size//2+1)]
    s=0
    ans=[]
    for x in coords: 
        l=[]
        for y in coords:
            val=math.exp(-1*(x**2 +y**2)/(2*sigma*sigma))
            l.append(val)
            s+=val
        ans.append(l)
    for i in range(size):
        for j in range(size):
            ans[i][j]=ans[i][j]/s
    return ans 