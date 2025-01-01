# Conditional Statements
## If/Else

print("Welcome to the rollercoaster!")
height =  int(input("What is your height in cm? "))

## if height >= 120:
##    print("You can ride the rollercoaster!")
## else:
##    print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
## > Greater than
## < Less than
## >= Greater than or equal to
## <= Less than or equal to
## == Equal to, if there is a single =, it will be an assignment operator
## != Not equal to

# Modulo
## % Modulo operator gives the remainder of a division
## 6 % 2 = 0
## 5 % 2 = 1, 5 divided by 2 is 2 with a remainder of 1
## 8 % 3 = 2, 8 divided by 3 is 2 with a remainder of 2
## Even numbers are divisible by 2, so the remainder will be 0
## Odd numbers are not divisible by 2, so the remainder will be 1

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

## The indentation is important in Python, 
## it is used to define the block of code.

# Nested if/else

## if height >= 120:
##   print("You can ride the rollercoaster!")
##    age = int(input("What is your age? "))
##    if age < 12:
##        print("Please pay $5.")
##    elif age <= 18: # 12 - 18
##       print("Please pay $7.")
##   else:
##        print("Please pay $12.")
## else:
##   print("Sorry, you have to grow taller before you can ride.")



# Multiple if/else statements in succession
print("Welcome to the rollercoaster!")
height =  int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Logical Operators
## and
num = int(input("Enter a number: "))
if test > 0 and test < 10:
    print("True")
else:
    print("False")
## or
if test > 0 or test < 10:
    print("True")  
else:
    print("False")
## not
if not test > 0:
    print("True")
else:
    print("False")
