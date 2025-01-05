# Function with inputs
def greet():
    print("Hello")
    print("How do you do?")
    print("Isnt the weather nice?")

greet()

# Add Variable to function
# Function that allows for inputs
# name is parameter
# Hal is the argument
def hello(name):
    print(f"Hello {name}")

hello("Hal")

# Example, life in weeks
def life_in_weeks(year):
    year_left = 90 - year
    total_weeks = 52 * year_left
    print(f"You have {total_weeks} weeks left.")
    
life_in_weeks(12)

# Positional vs Keyword Arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Hal", "Indonesia")
# If we switch the position, it will gives us "Hello Indonesia" "What is it like in Hal", its called positional argument
# If we dont want this to happen, we can use keyword argument.

greet_with(location= "Bali", name= "Dimas")