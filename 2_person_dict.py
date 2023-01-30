person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] # value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} # value is a dictionary


# print out name of the second child
print(person["children"][1])

# print out name of the cat
print(person["pets"]['cat'])

# iterate through all children and print out each child
for child in person['children']:
    print(child)

# print out the pets in the format:

# type of pet: dog name of pet: Fido