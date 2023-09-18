from typing import List

def prints(x,arr):
    if x == 0:
        return
    arr.append(x)
    prints(x-1,arr)
    
def printNos(x: int) -> List[int]: 
    # Write your code here
   arr = []
   prints(x,arr)
   return arr