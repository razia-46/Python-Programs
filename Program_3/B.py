"""
Question:
- Write a program to create, concatenate, and print a string, and accessing a substring from a given string.
"""


str1 = "Welcome to"
str2 = "Python Programming Lab  "
str3 = str1 + str2
print("The new concatenated string is " + str3)  

str4 = "abc"
print("The original string is : " + str4)

res = [str4[i: j] for i in range(len(str4)) for j in range(i + 1, len(str4) + 1)]
print("All substrings of string are : " + str(res))
