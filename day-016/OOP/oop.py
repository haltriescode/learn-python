# OOP

# In OOP, If we have an object, we should define what it has, and what it does
# what it has => attributes
# what it does => methods
# object's blueprint => Class

# Constructing object and access atributes and methods
from turtle import Turtle, Screen
timmy = Turtle() # timmy is our new object
print(timmy)

timmy.shape("turtle")
timmy.color("coral") # calling method
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) # Calling attributes
my_screen.exitonclick()


