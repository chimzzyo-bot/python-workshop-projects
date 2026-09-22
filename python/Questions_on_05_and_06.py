number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Negative")

num = int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

Age = int(input("Enter your age: "))
if Age>=18:
    print("You are an adult")
else:
    print("You are a minor.")

password = "python123"
p = input("Enter the password: ")
if p == password:
    print("Access granted")
else:
    print("Access denied")

score = int(input("Enter your score: "))
if score>=70 and score<=100:
    print("A")
elif score>=60 and score<=69:
    print("B")
elif score>=50 and score<=59:
    print("C")
elif score>=45 and score<=49:
    print("D")
else:
    print("F")


num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

if num1>num2:
    print("num1 is greater than num2")
elif num1 == num2:
    print("They are equal")
else:
    print("num2 is greater than num1")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
op = input("Enter sign operator: ")

if op == '+':
    print("Result: ", num1+num2)
elif op == '-':
    print("Result: ", num1-num2)
elif op == '*':
    print("Result: ", num1*num2)
elif op == '/':
    if num2==0:
        print("Math error. The denominator should not be zero")
    else:
        print("Result: ", num1/num2)
else:
    print("invalid operator")


temp = int(input("Enter a temperature in degrees: "))
if temp>30:
    print("It's hot")
elif temp>=20 and temp<=30:
    print("It's warm")
elif temp>=10 and temp<=19:
    print("It's cool")
else:
    print("It's cold")

def greet(name):
    print("Hello, ", name)
    print("Welcome to Python.")

greet("Chimzzy")

def check_number(number):
    if number%2==0:
        print("Even")
    else:
        print("odd")
num = int(input("Enter a number: "))
check_number(num)

def check_age(age):
    if age<13:
        print("child!")
    elif 13<= age <=17:
        print("Teenager")
    else:
        print("Adult")
a = int(input("Enter your age"))
if a < 0:
    print("Invalid number")
else:
    check_age(a)

def get_grade(score):
    if score>=70 and score<=100:
        return "A"
    elif score>=60 and score<=69:
        return "B"
    elif score>=50 and score<=59:
        return "C"
    elif score>=45 and score<=49:
        return "D"
    else:
        return "F"
get_grade(63)

def login(username, password):
    correct_username = "admin"
    correct_password = "python123"

    if username==correct_username and password==correct_password:
        print("Login successful")
    elif username!= correct_username:
        print("Incorrect username")
    else:
        print("Incorrect password")