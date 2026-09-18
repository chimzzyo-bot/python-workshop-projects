name = 'John Doe' # This is a variable
age = 25
my_variable_name = 'freeCodeCamp'


# This is a single-line comment

# This is a
# multi-line
# comment

my_integer_var = 10
print('Integer:', my_integer_var)
print(type(my_integer_var))

# You use isinstance() to check if a variable matches a specicific data type

age1 = False #integer
print(isinstance(age1, str))
#To check for either of the da)ta types you use isinstance(variable,(dtype,dtype))
print(isinstance(age1,(str,int)))

#bool is a subclass of int so it would return int
