from math import *

n = int(input())
flag = 1
if n > 1:
    for i in range(2,ceil(sqrt(n))):
        if n % i == 0:
            flag = 0
            break
    if flag == 0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")

#using func
# def check_prime(n):
#     if n == 1:
#         return 'NO'
#     for i in range(2,ceil(sqrt(n))):
#         if n % i == 0:
#             return 'NO'
#     return 'YES'

# n = int(input())
# res = check_prime(n)
# print(res)