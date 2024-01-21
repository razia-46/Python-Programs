"""
Question:
- Write a Python program to check whether the given string is a palindrome or not.
"""
def isPalindrome(s):
    return s == s[::-1]


s = "Razia Khatoon"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
