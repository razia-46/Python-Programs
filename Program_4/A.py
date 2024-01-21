# List Operations

"""
Create a list
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
Add an item at a specified index
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""
Get the length of a list
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Add an item to the end of the a list
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""
Remove an item
"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""
Remove the last item
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""
Remove an item at a specified index
"""
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""
Empty list
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
