from typing import *

def reverse(i,n,nums):
    if i >= n//2:
        return nums
    temp = nums[n-1-i]
    nums[n-1-i] = nums[i]
    nums[i] = temp
    return reverse(i+1,n,nums)

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    reverse(0,n,nums)
    return nums
    pass

# another method
# from typing import *

# def reverseArray(n: int, nums: List[int]) -> List[int]:
#     # Write your code here
#     def rev(n,nums,arr):
#         if n == 0:
#             return 
#         arr.append(nums[n-1])
#         return rev(n-1,nums,l)
    
#     arr = []
#     rev(n,nums,arr)
#     return arr
#     pass