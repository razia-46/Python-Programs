"""
Question:
- Write a Python program to display all the prime numbers in a given interval.
"""

lower, upper = 2, 15
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
