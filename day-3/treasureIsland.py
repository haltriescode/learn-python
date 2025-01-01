print("********************************")
print("         __________  ")
print("        /\____;;___\ ")
print("       | /         / ")
print("       `. ())oo() . ")
print("        |\(%()*^^()^\ ")
print("       %| |-%-------| ")
print("      % \ | %  ))   | ")
print("      %  \|%________| ")
print("                      ")
print("********************************")
## We can also use triple quotes to print the ASCII art
print("Welcome to Treasure Island.")
print("********************************")
print(''' 
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

''')
print("Your mission is to find the treasure.")
left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. \nThere is an island in the middle of the lake. \nType 'wait' to wait for a boat. \nType 'swim' to swim across.\n")
    if swim_or_wait == "wait":
        red_yellow_blue = input("You arrive at the island unharmed. \nThere is a house with 3 doors. One red, one yellow and one blue. \nWhich colour do you choose?\n")
        if red_yellow_blue == "yellow":
            print("You found the treasure! \nYou win!")
        elif red_yellow_blue == "red":
            print("It's a room full of fire. \nGame Over.")
        elif red_yellow_blue == "blue":
            print("You enter a room of beasts. \nGame Over.")
        else:
            print("You chose a door that doesn't exist. \nGame Over.")
    else:
        print("You got attacked by an angry trout. \nGame Over.")
else:
    print("You fell into a hole. \nGame Over.")

