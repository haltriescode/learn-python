# Let say we have a bug

def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")

my_function()

# To solve this, we need to:
# Describe the Problem - Write your answer as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

# The problem here, the code never touch 20
# Solution
def my_new_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")

my_new_function()

#Reproduce the bug
from random import randint
dice_images = ["1","2","3","4","5","6"]
dice_num = randint(1,6)
print(dice_images[dice_num])

#to fix this, we can try to reproduce the bug by write the dice_num manually
#dice_num = 1
#dice_num = 2
#dice_num = 3
#dice_num = 4
#dice_num = 5
#dice_num = 6

#from this we will know where the bug is, and can solve it after that
#dice_num = randint(0,5)



# Play Computer - Pretending to be a computer

year =int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# check the code line by line
# year = 1994
# if year > 1980 (True) and year < 1994 (False) >>> if False (print is skipped)
# elif year > 1994 (False) >>> elif False (print is skipped again)
# Thats why the code didnt print anything.
# The problem occurs because there isnt actually a bucket that catches 1994
# we can fix it by edit the code:
# elif year >= 1994



#Fixing Errors and Watch for Red Underlines
age = int(input("How old are you?"))
if age > 18:
    print("You can drive ate age {age}.")

#When the user input eleven instead of 11, it will generate error 
# ValueError: invalid literal for int() with base 10: 'eleven'
# The easy solution for this error is simply by tell user not to do that
# But we can also use try and except, so the program didnt stop suddenly

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical number like 15.")
    age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")

#Now user can get feedback when inputted wrong input, and they can write input again.
#But remember, solving Error doesnt always fix our bugs
#We still have a bug, "You can drive at age {age}.". The inpputed age doesnt pass to the output text.

# In this case, we have to relly on our skill as programmer. The more bugs we solve, the better we get at it.
# Solution: print(f"You can drive at age {age}.")


# Squash bugs with a print()
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
# Print is our friend
# The problem on the code above is that it prints 0, not the end value of calculation.

# To check where the broken code is, we can print each variable

# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")

# Turns out word_per_page is 0 (default value)
# Instead of using assignment (=) we use equal (==) sign
# Solution, word_per_page = int(input("Number of words per page: "))



# Using Debugger
# click the red button on the left of the code line's number (Its 111 for this line)
# create a breakpoint
# run python debugger


# Final Tips: 
# take a break
# Ask a friend
# Run the code often
# Ask Stackoverflow

