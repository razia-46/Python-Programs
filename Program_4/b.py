"""
Create and print a dictionary
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

"""
Accessing Items
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

"""
Using get() Method
"""
print("Get the value of the model key:")
x = thisdict.get("model")

"""
Change values
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2022

"""
Print the number of items in the dictionary
"""
print(len(thisdict))

"""
Empty dictionary
"""
mydict = {}
