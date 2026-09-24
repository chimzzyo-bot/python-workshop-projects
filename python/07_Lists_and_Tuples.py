cities = ['Los Angeles', 'London', 'Tokyo']

print(cities[2])

#Negative indexing is used to access elements starting from the end of the list instead of the
# beginning at index 0. To access the last element of any list, you can use -1 like this:

print(cities[-1])

#Another way to create a list is to use the list() constructor.
# The list() constructor is used to convert an iterable into a list like this:

developer = "Chimzzy"
print(list(developer))

#To get the total number of elements in a list, you can use the len() function like this:
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # 5

#If you wanted to update a value at a particular index, you can do something like this:
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

#deletion: If you want to remove an element from a list you can use the del keyword like this:

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

#To check: Sometimes it is helpful to check if an element is inside the list.
# To do that, you can use the in keyword like this:

#Nested lists
developers = ["nadia", "Ama", ["onion", "onimd"], ["were", "oper"]]
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

#In this example, we have one nested list containing three popular programming languages.
# To access the nested list, you will need to access it using index 2 since lists are zero
# based indexed:

print(developer[2]) # ['Python', 'Rust', 'C++']

#Then to access the second language from that nested list, you will need to access it
# using index 1 like this:

print(developer[2][1])

#Unpacking a list: Unpacking values from a list is a technique used to assign values
# from a list to new variables. Here is an example of unpacking a developer list into
# new variables called name, age and job.

name, age,job = developer
print(job)
print(name)
print(age)

developeri = ['Alice', 34, 'Rust Developer']
name, *rest = developeri

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

#Slicing operator
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']

#Step interval in slicing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) #not putting anything in the middle allows it to go through all the numbers
print(numbers[1:4:2]) #[2,4]

#append(), pop(), and sort()
#The first method we will look at is the append() method.
# This is used to add an item to the end of the list.
numbers.append(7)
print(numbers) # [1, 2, 3, 4, 5, 6]

even_numbers = [9, 8, 10, 11]
numbers.append(even_numbers)
print(numbers)

#Notice how the entire even_numbers list is nested inside of the numbers list.

numbers.extend(even_numbers)
print(numbers)

#insert an element
#To insert an element at a specific index in a list, you can use the insert() method.
# This method accepts two arguments: the index where you wish to insert the new item and
# the item you want to insert.

numbers.insert(2,5)
print(numbers)

#remove an element
numbers.remove(5)
print(numbers)

#To remove an element at a specific index in the list,
# you can use the pop() method like this:

numbers.pop(3)#using their index number to remove it
print(numbers)

#If you need to empty the list, then you can use the clear() method like this:
numbers.clear()

print(numbers) # []

#The next method we will take a look at is the sort() method. This method is used to sort
# the elements in place. Here is an example of sorting a random list of numbers in place:

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

#In contrast to the sort() method, there is the sorted() function which works for any
#iterable and returns a new sorted list instead of modifying the original list. For example:

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]


#The next method we will take a look at is the reverse() method. This method, will reverse
# a list of elements in place like this:

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers)

#Index
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # 1

##############    Tuple    ################

developer = ('Alice', 34, 'Rust Developer')
#To access an element from a tuple, you can use bracket notation and the index number:
print(developer[1]) # 34

#If you need to access elements starting from the end of a tuple,
# then you can use negative indexing.

numbers = (1, 2, 3, 4, 5)
print(numbers[-2]) # 4

#How you create a tuple
name = "chimzzy"
print(tuple(name))

#To check if an item is in a tuple, you can use the in keyword like this:
programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages )# True
print('JavaScript' in programming_languages )# False

#basically what you can use for lists you can do it with tuples

# but If you need to remove an item from a tuple, that isn't possible because tuples
# are immutable. So this example, will produce an error:
developer = ('Jane Doe', 23, 'Python Developer')
#del developer[1]

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: "tuple" object doesn't support item deletion
"""

#Count how elements are in the tuple
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2

#index searching
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2

#Now the result is index 2 because we are starting the search at index 2, and searching
# up to, but not including, index 5.

#If you need to customize the sorting behavior for an iterable, you can use the optional
# reverse and key arguments. Here is an example of using key argument to sort items in a tuple by length:

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

#reverse
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']

