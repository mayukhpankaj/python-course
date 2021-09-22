
""" strings in python are surrounded by single or double qoutes ' / " """ 

name = 'may'

age=20

# concatenate  

""" cast to strings before concatenation """

# msg = name + ' is '+ str(age)+' years old'

# print(msg) 

""" arguments by postion """

# print('My name is {nm} & im {yr} years old.'.format(nm=name,yr=age))



""" #fstring 3.6+ """

print(f'Hello, my name is {name} and I am {age} years old.')


""" capitalize, 1st letter """

s = 'hello world'

print(s)

print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.swapcase())

print(len(s))

print(s.replace('world', 'guyzz'))

#count no. of sub string in the string 

print(s.count('l'))

#check string start or ends with a substring

print(s.startswith('hello'))
print(s.endswith('.'))

# subring dictionary 
print(s.split())

#get position 

print(s.find('h'))


print(s.isalpha())  #false bcoz of space 

print(s.isnumeric())







