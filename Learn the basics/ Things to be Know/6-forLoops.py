n = int(input())
l = [1,1]
for i in range(n-2):
    l.append(l[-1] + l[-2])
print(l[n-1])