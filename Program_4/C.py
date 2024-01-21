"""
Create a tuple
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Add Items
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

"""
Check if a tuple item exists
"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

"""
Access tuple items
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""
Loop through a tuple
"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

"""
Get the length of a tuple
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
