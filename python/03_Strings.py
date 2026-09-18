#If your string contains either single or double quotation marks, then you have two options:

#Use the opposite kind of quotes. That is, if your string contains single quotes, use double
# quotes to wrap the string, and vice versa:

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

print("h" in msg)
print("sun" in msg)

my_str = 'Hello world'
print(len(my_str))

print(msg[0])
print(msg[-1])
print(msg[2])
print(msg[4])

#concatenation
First_name = "Chimzzy"
Second_name = "Ogwutum"

name = First_name + " " + Second_name
print("My name is", name)

#repeated strings
Laugh = 'Ha'
repeat_laugh = Laugh*3
print(repeat_laugh)

#converting an integer to string
age = 18
name_and_age = name +  str(age)
print(name_and_age)

#String interpolation
names = 'Chimzzy Ogwutum'
ages= 18
n_a_a = f'My name is {names} and i am {ages} years old'
print(n_a_a)

#String Slicing
my_str = 'Hello world'
print(my_str[1:4]) # ell
#note that it starts from 1 and ends at 3 4 is non-inclusive

my_str = 'Hello world'
print(my_str[:7])  # Hello w
#This extracts everything from index 0 up to (but not including), the character at index 7
print(my_str[8:])  # rld
print(my_str[:])  # Hello world

#string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2]) #0,2,4,6,8,10 basically

print(my_str[::-1]) # dlrow olleH you can reverse it like this

my_str = 'hello world'

#upper and lower case
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

lowercase_my_str = my_str.lower() #hello world
print(lowercase_my_str)

#trimming a word
mystr = '    helllooo    '
s = mystr.strip()
print(s)

#replacing a word or letter with another using word.replace(old,new)

m = mystr.replace('   ', ' yuyu')
print(m)

#splitting a word
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

#joining two strings in array
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)

#Starts with and ends with boolean
print(my_str.startswith('h'))
print(my_str.endswith('hello'))

#.find() searches a string for another string and tells you the index (position)
# where it starts. -1 means the thing you're searching for wasn't found.

my_str = 'hello world'

world_index = my_str.find('world')
print(world_index) #6

#capitalize(): Returns a new string with the first character capitalized
# and the other characters lowercased.
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

#isupper(): Returns True if all letters in the string are uppercase and False if no
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

#islower(): Returns True if all letters in the string are lowercase and False if not.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True

#title(): Returns a new string with the first letter of each word capitalized.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World





