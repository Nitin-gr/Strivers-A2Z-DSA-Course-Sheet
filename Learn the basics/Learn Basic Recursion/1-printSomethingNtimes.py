def printNos(x: int) -> list[int]: 
    # Write your code here
    arr = [x]
    if x > 1:
        arr = printNos(x-1) + arr
    return arr


# another approach
# from typing import List
#
# def num(x,arr):
#     if x < 1:
#         return arr
#     num(x-1,arr)    
#     l.append(x)
#
# def printNos(x: int) -> List[int]: 
#     # Write your code here
#     arr = []
#     num(x,arr)
#     return arr
#     pass