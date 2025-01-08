# Randomisation Module
# Generate pseudo-random numbers
import random

# range(1, 7) generates random numbers between 1 and 6
random_integer = random.randint(1, 6)
print(random_integer)

# what is module?
## A module is a file containing a set of functions you want to include in your application.
## Module are made up of functions, classes and variables.
## It is a way to organize code into separate files.
## You can also use modules that someone else has written.
## Modules are used to make the code more readable and maintainable.

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# Multiply the random number by 5
random_number_0_to_5 = random_number_0_to_1 * 5
print(random_number_0_to_5)

## By multiplying the random number by 5, 
## we get a random number between 0 and 4.999999999999999
## To get a random number between 0 and 5,
## we can use the floor division operator (//) to round down the number.

random_number_0_to_5_rounded = random_number_0_to_5 // 1
print(random_number_0_to_5_rounded)

# Heads or Tails
## Write a simple program that simulates a coin toss.

## 1. Generate a random number between 0 and 1.
## 2. If the random number is 0, then it's Heads.
## 3. If the random number is 1, then it's Tails.

random_number_0_to_1 = random.randint(0, 1)
if random_number_0_to_1 == 0:
    print("Heads")
else:
    print("Tails")

# Lists
## A data structure to store multiple values in one variable.
## Lists are defined by square brackets [].
## Lists can contain any data type.
## Lists can contain different data types.
## Lists have order.

fruits = ["Apple", "Orange", "Banana"]
print(fruits[0]) # Apple
print(fruits[-1]) # Banana, negative indexing, starts from the end of the list.

## change the value of an item in the list
fruits[2] = "Pineapple"
print(fruits) # ['Apple', 'Orange', 'Pineapple']

## add an item to the list
fruits.append("Mango")
print(fruits) # ['Apple', 'Orange', 'Pineapple', 'Mango']

## There are many methods that can be used with lists.
## https://docs.python.org/3/tutorial/datastructures.html
## we can use documentation to find out more about the methods that can be used with lists.

# Who's Paying The Bill?
## Write a program that will select a random name from a list of names to pay the bill.

friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
## First option, using random.choice method
print(random.choice(friends)) # random.choice() method selects a random item from the list.

## Second option, using random.randint() method
random_index = random.randint(0,4)
print(friends[random_index])

# Index Errors
## IndexError occurs when you try to access an index that does not exist.
## For example, if you have a list with 3 items, the indexes are 0, 1, 2.
## If you try to access index 3, you will get an IndexError.

state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
## if we try to access index 50, we will get an IndexError.
## print(state_of_america[50])

## to avoid IndexError, we can use the len() function to get the number of items in the list.
## and then subtract 1 from the number of items to get the last item in the list.
number_of_states = len(state_of_america) # 50

print(state_of_america[number_of_states - 1]) # Hawaii

# Nested Lists
## A list within a list.
## Nested lists are useful for representing more complex data structures.
## Example: A list of vegetables and fruits.

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

## A list of fruits and vegetables
dirty_dozen = [fruits, vegetables] #dirty_dozen is a nested list
print(dirty_dozen) # [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

## Accessing items in a nested list
print(dirty_dozen[0][1]) # Nectarines
print(dirty_dozen[1][0]) # Spinach
print(dirty_dozen[1][1]) # Kale

