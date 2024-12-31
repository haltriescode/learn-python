# Primitive data types

## Subscripting
print("Hello"[0])  # H

## String
print("123" + "345") # 123345

## Integer
print(123 + 345) # 468

## Large integer
print(123_456_789) # 123456789

## Float = Decimal number = Floating point number
print(3.14159) # 3.14159

## Boolean
print(True)
print(False)

# Type error
## num_char = len(input("What is your name?"))
## We can't concatenate string with integer

# Type Checking
type("Hello") # <class 'str'>
type(123) # <class 'int'>
type(3.14159) # <class 'float'>
type(True) # <class 'bool'>

# Type conversion
## String to integer
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

## Integer to string
two_digit_number = input("Type a two digit number: ")
number = int(two_digit_number)
print(number + 100)

## Mathematical operations
print("My age is " + str(23) + " years.")
print(3 + 5) # 8
print(7 - 4) # 3
print(3 * 2) # 6
print (6 / 3) # 2.0 the data is automatically converted to float
print(2 ** 3) # 8 # 2^3 (2 to the power of 3)
print(3 // 2) # 1 # floor division

# Number manipulation
bmi = 84 / 1.65 ** 2
print(bmi) # 30.8

## Converting float to integer
print(int(bmi)) # 30

## Round function
print(round(bmi)) # 31

## Round function with precision
print(round(bmi, 2)) # 30.86

# Assignment operators
score = 0

## User scores a point
score = score + 1
print(score) # 1

# F string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

