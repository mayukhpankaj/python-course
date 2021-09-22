# A dictionary is a collection unordered changeable and indexed
# NO DUPLICATE


# create dict

person = {
      
      'first_name': 'may',
      'last-_name': 'punk',
      'age': 30 
}


#use a constructor

num = dict(x=1,y=2)

print(person['first_name'])

#add key/value 

person['phone'] = '91999999'

#get dict keys & items 

# print(person.keys())

# print(person.items())

"copy dict"

person2 = person.copy()

person2['city']='NY'

# remove item 

# del(person['age'])
# person.pop('phone')


# clear dict 
# person.clear()

#length of dict

print(len(person2))


#list of dict 

people = [person, person2]

print(people)
print(people[1]['city'])

print(person)