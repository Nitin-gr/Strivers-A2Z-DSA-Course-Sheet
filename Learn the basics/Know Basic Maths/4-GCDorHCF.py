def calcGDC(n:int, m: int) -> int:
    #Write your code here
    a = max(n,m)
    l = []
    for i in range(1,a+1):
        if n % i == 0 and m % i == 0:
            l.append(i)
    return max(l)
    pass

#more optimal code
# def calcGDC(n:int, m: int) -> int:
#     if m == 0:
#         return n
#     else:
#         return calcGDC(m,n%m)
#     pass