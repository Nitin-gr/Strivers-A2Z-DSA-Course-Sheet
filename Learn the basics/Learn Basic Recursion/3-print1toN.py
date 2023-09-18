from typing import List

def num(x,arr):
    if x < 1:
        return arr
    num(x-1,arr)    
    arr.append(x)
    
def printNos(x: int) -> List[int]: 
    # Write your code here
    arr = []
    num(x,arr)
    return arr
    pass

# another approach
# def rec(x,l):
#     if x==0:
#         return
#     rec(x-1,l)
#     l.append(x)
    
# def printNos(x: int) -> list[int]: 
#     # Write your code here
#    l = []
#    rec(x,l)
#    return l