from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    
    def fact(number):
        if number==0:
            return 1
        else:
            return number*fact(number-1)
    result = []
    num = 1
    while True:
        f = fact(num)
        if f <= n:
            result.append(f)
            num += 1
        else:
            break
    return result
    pass