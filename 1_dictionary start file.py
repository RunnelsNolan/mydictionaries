import random

phonebook = {}
# create empty dictionary ^
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
# 3 key value pairs ^^^

'''

print()
print('*****  start section 1 - print dictionary ********')
print()
mydictionary = dict (m=9, n=9)
print(mydictionary)
# creating dictionary^

print(len(phonebook))
print(type(phonebook))
# ^^ Printing the length and type of the dictionary

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'
if name in phonebook:
    print(phonebook{name})
else:
    print(f"{name} is not in phone book")
#print(phonebook["Chris"])
# ^^ you gave it the key and will return its value, its CASE sensitive




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'
print(phonebook)



print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"the key is {key} and the value is {phonebook[key]}")

# .values() method gives the values for each key value pair
for value in phonebook.values():
    print(value)

for key, value in phonebook.items:
    print(f"the key is {key} and the value is {value}")

# if you specify ONLY 1 value the output is a tuple, but with 2 it splits it
for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris', '999') # if it doesn find Chris it gives it a default value of 999
print(phone)

phonebook.clear()
print(phonebook) # clears out phonebook but DOESNT DELETE the dictionary


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found') # if it cant find/ pop chris it can send a default message
print(remove)
print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()

print(a)
print(phonebook)
print()



print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook)
print(phonebook_list)
random_key = random.choice(phonebook_list)
print(random_key, phonebook[random_key])

print(phonebook[random.choice(list(phonebook))]) # 6 lines above made in more line

print()
print('*****  end section 9 ********')
print()




