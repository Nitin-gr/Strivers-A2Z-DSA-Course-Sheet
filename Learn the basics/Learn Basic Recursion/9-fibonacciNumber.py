def generateFibonacciNumbers(n: int) -> list[int]: 
    # Write your code here
    def fibo(num):
        if num==0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibo(num-1)+fibo(num-2)
    
    arr = []
    for i in range(n):
        f = fibo(i)
        arr.append(f)
    return arr
    pass

# more efficient for large inputs and more optimal
# from typing import List

# def generateFibonacciNumbers(n: int) -> List[int]: 
#     # Write your code here
#     f = [0,1]

#     for i in range(2,n):
#         f.append(f[i-1]+f[i-2])
#     return f[:n]
#     pass