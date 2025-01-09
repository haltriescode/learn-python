# local vs global scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Output will be 
#enamies : 2
#enemies : 1

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength) # output will be 2

drink_potion()
# print(potion_strength) # error, you can only access it inside function

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health) # we can access player_health, because its global scope

drink_potion()
print(player_health)



# There is no Block Scope in Python!
# Variables created inside blocks (if, for, while) are accessible outside those blocks
# Only functions create new scopes in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modify Global Scope

enemies = "Skeleton"

def increase_enemies():
 #   global enemies #We have to explicitely define the variable #not recommended
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# or we can just call it as return value

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



# Python Constants and Global Scope

pi = 3.14159
GLOBAL_URL = "www.123.com" #You can write variable name on full capital to differenciate it

def my_function():
    print(GLOBAL_URL)