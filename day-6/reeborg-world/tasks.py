# First Task
# Make Reeborg turn right
# web page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Second Task
# Make Reeborg make a square
# web page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Third Task
# Hurdle 1
# Make Reeborg jump over the hurdle
# web page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()

# Fourth Task
# Hurdle 2
# Make Reeborg jump over the hurdles until it reaches the finish line
# web page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

while not at_goal(): # at_goal() is a function that returns True if Reeborg is at the goal, otherwise False
    jump()

# Fifth Task
# Hurdle 3
# Make Reeborg jump over the hurdles. This time, Reebrorg will have to jump over the random placed hurdles until it reaches the finish line
# Website: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# First, modify jump() function, remove the first move() function
def jump(): 
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Sixth Task
# Jumping over the hurdles with variable heights
# Make Reeborg jump over the hurdles with variable heights until it reaches the finish line
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Modify jump() function, add a while loop to check if there is a wall on the right side of Reeborg
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Seventh Task
# Maze
# Make Reeborg find the exit in the maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

