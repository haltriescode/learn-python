print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif pepperoni == "N":
    pass
else:
    print("Invalid input.")

if extra_cheese == "Y":
    bill += 1
elif extra_cheese == "N":
    pass
else:
    print("Invalid input.")

print(f"Your final bill is: ${bill}.")