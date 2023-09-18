def palindrome(stri,n,i):
    if i > n//2:
        return True
    if stri[i] != stri[n-i-1]:
        return False
    return palindrome(stri,n,i+1)

def isPalindrome(string: str) -> bool:
    n = len(string)
    return palindrome(string,n,0)
    pass

# another method
# def isPalindrome(string: str) -> bool:
    
#     n = len(string)
#     def reversestring(i):
#         if i > n // 2:
#             return True
#         if string[i] != string[n - i - 1]:
#             return False
#         return reversestring(i + 1)
#     return reversestring(0)
#     pass