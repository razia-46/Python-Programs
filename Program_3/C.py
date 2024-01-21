def printme(str):
    """
    This function prints the passed string. 
    What happens when you call this function with different strings?
    """
    print(str)

# Now you can call printme function
printme("I'm the first call to the user-defined function!")
printme("Again second call to the same function")


print("Argument Example")
def my_function(fname):
    """
    This function appends 'khan' to the given name. 
    How does the function behave with different names?
    """
    print(fname + " khan")

my_function("Saba")
my_function("Salman")
my_function("Zohran")


def f():
    """
    This function demonstrates the scope of a variable inside a function.
    What happens to the variable 's' in local and global scopes?
    """
    # local scope
    s = "Me too."
    print(s)

    # Global scope
    s = "I love Python"
f()
print(s)

def my_func():
    """
    This function illustrates the scope of a variable inside and outside a function.
    What values does the variable 'x' hold inside and outside the function?
    """
    # local scope
    x = 10
    print("Value inside function:", x)

    # Global scope
x = 20
my_func()
print("Value outside function:", x)


def factorial(x):
    """
    This recursive function calculates the factorial of a number.
    What happens when you call this function with different values of 'x'?
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = 3
print("The factorial of", num, "is", factorial(num))

