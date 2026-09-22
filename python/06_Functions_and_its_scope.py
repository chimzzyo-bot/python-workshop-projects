#Prompting a user to enter something
name = input('What is your name?') # User types "Kolade" and presses Enter
print('Hello', name) # Output: Hello Kolade

def hello():
    print('Hello World')

#To run the function, you need to call it with its name followed by a pair of parentheses:

def calculate_sum(a, b):
    print(a + b)

#You can see that our function, calculate_sum, has a and b in its parentheses, separated
# by a comma. Those are called parameters. Think of parameters as placeholder variables
# that act as "slots" for the values you pass into functions when you call them.

#To use the parameters, you have to pass in "arguments". Arguments are the values you pass
# to a function when you call it.

calculate_sum(3, 1) # 4
#If you call the function without the correct number of arguments, you'll get a TypeError:

calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

#You can see that the calculate_sum function prints the sum of a and b,
# but it doesn't return anything explicitly. So when we assign its result to my_sum,
# the value is actually None. To fix that, you can use the return keyword to send back
# the result:

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4

#Scope determines where you can use a variable in your code.

#Python has additional scope rules. For now, focus on local and global scope.

#A variable created outside a function has global scope. You can use it both inside and
# outside functions.

#A variable created inside a function has local scope. You can only use it inside that function.
# Function parameters are local variables too.

tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
print(tax) # NameError: name 'tax' is not defined
