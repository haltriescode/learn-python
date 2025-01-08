# Python Dictionary

programming_dictionary = {
    "Bug" : "An error in program that prevents the program from running as expected",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again.",
    }

print(programming_dictionary["Bug"])

# Change dictionary content

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Nesting
# Each key should only return one type of item data, so we can store items inside list.

capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#print Lille
print(travel_log["France"][1])

# Nested list in another list

nested_list = ["A", "B", ["C","D"]]
print(nested_list[2][1])

# Nest dictionary within dictionary

travel_log = {
    "France" : {
        "cities_visited": ["Paris", "Lille", "dijon"],
        "total_visits": 8,
    },
    "Germany": {
    "cities_visited":["Stuttgart", "Berlin", "Hamburg"],
    "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])


