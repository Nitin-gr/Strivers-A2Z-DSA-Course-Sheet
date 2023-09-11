number = int(input())
copy = number
size = len(str(number))
ans = 0
while number > 0:
    num = number % 10
    ans += pow(num,size)
    number = number // 10
if copy == ans:
    print("true")
else:
    print("false")