print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill * tip / 100 + bill
each_person = total_bill / people

print(f"Each person should pay: ${round(each_person, 2)}")