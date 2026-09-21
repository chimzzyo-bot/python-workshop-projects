#==	Equal	Checks if two values are equal
#!=	Not equal	Checks if two values are not equal
#>	Greater than	Checks if the value on the left is greater than the value on the right
#<	Less than	Checks if the value on the left is less than the value on the right
#>=	Greater than or equal	Checks if the value on the left is greater than or equal to the value on the right
#<=	Less than or equal	Checks if the value on the left is less than or equal to the value on the right

age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal

if age:
    pass # Code to execute if condition is True
else:
    pass # Code to execute if condition is False


age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('blahblah')



is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')


is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
