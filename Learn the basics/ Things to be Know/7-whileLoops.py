n=int(input())
a = []
b = []
while(n > 0):
    num = n % 10
    n = n // 10
    if num % 2 == 0:
        a.append(num)
    else:
        b.append(num)
print(sum(a)," ", sum(b))