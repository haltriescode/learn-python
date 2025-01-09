# Function with output

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("ANdi", "RamaDHan")
print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2( function_1("hello"))

print(output)

# multiple return
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your fist name?"), input("What is your last name?")))

# Docstring
# To make a docstring you should use three quote marks """"""
# We caan make multiple line of comment with this

"""This is a Comment
    This is also a comment
    This also is a comment"""