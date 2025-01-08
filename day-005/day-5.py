# Loop

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + " is a fruit")

print(fruits)

## Highest Score
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

## Using Max function
print(f"The highest score in the class is: {max(student_scores)}")

# for loop with range
## range should be used with for loop
for number in range(1, 11):
    print(number)

# for loop with step
for number in range(1, 11, 2): # 2 is the step
    print(number)

# Gauss formula
total = 0
for number in range(1, 101):
    total += number
print(total)

# FizzBuzz


