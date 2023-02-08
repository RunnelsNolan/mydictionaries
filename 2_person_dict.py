person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] # value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} # value is a dictionary


# print out name of the second child
print()
print(person["children"][1]) # use INDEX # because its a LIST
print()

# print out name of the cat
print(person["pets"]['cat']) # use KEY because its a Dictionary
print()

# iterate through all children and print out each child
for child in person['children']:
    print(child)
print()

# print out the pets in the format:
# type of pet: dog name of pet: Fido
for key, value in person['pets'].items():
    print(f'type of pet: {key} name of pet: {value}')

print()
