from art import logo

print(logo)
first_number = int(input("What's the first number?: "))
print(
'''
+
-
*
/
'''
)
operator = input("Pick an operation: ")
sec_number = int(input("What's the next number?: "))

def calculator(a,b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a / b
    elif operator == "*":
        return a * b
    else:
        "Wrong input"
output = calculator(first_number,sec_number)
print(f"Output: {output}")
