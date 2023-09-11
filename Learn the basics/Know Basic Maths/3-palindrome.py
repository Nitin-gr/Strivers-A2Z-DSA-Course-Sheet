n=int(input())  
copy = n
string = ""
while n > 0:
    num = n % 10
    string = string + str(num)
    n = n // 10
if copy == int(string):
    print("true")
else:
    print("false")

#code with python stl
# n=int(input())  
# s = str(n)
# print(str(s == s[::-1]).lower())
