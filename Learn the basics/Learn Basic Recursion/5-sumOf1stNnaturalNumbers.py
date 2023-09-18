#more compact code
from typing import List

def sumFirstN(n: int) -> int:
    
    # Write your code here.
    if n == 0: 
        return 0
    return n + sumFirstN(n-1)
    pass

# another approach
# def nsum(n,l):
#     if n == 0:
#         return 
#     l.append(n)
#     nsum(n-1,l)

# def sumFirstN(n: int) -> int:
    
#     # Write your code here.
#     l = []
#     nsum(n,l)
#     return sum(l)
#     pass
