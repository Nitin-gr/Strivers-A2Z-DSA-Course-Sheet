def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    arr = []
    cpy = n
    while n>0:
        for i in range(1,cpy+1):
            if n%i == 0:
                arr.append(i)
        n = n-1
    return sum(arr)
    pass