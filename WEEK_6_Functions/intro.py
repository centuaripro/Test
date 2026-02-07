
# Functions are named, reuseable blocks of code that performa specific task that organizes your program into smaller, manageable parts.

# - Understand what functions are and why they are eesential.
# - Define and call functions with parameters.
# - Use return values to get results from functions.
# - Write functions with default parameters.
# - Apply functions to solve data science problems.
# - Organize code with reusuable function libraries.

print("\n I am above the function")

def test ():
    print("\n I am inside the function")
    print("\n This is another line inside the function")

# CALL/EXECUTE THE FUNCTION
test()

print("\n I am below the function")

def add(a,b): # When defining a function,the place-holder variables you place in between the bracket is called a parater
    print(a + b)
    tuple = (a,b)
    print(tuple)
# print(a)
# print(a)

# Variable Scope
add(20,9) # When you call afunction, the values you place in between the brackets are called arguments
add(13,48)
add(98,14)

# Afunction being assigned to a variable

addition = add

# Pass a function as an argument to other functions
def operations(a,args):
    return a(*args)

operations(add, [12,5])

# Return a function from anothe rfunction

def _operation():
    def addition(values):
        return sum(values)
    return addition

result = _operation()([12,5])
print(result)
    