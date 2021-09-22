
""" 
like arrays 
list is a collection which is ordered changeable can be duplicates 
index starts with zero 0 
"""

""" create list"""

# numbers = [1,2,3,4]

# """ use a constructor """

# num2 = list((1,2,3,4))

# print(numbers,num2)


fruits = ['apple','orange','mango']

print(fruits[0])

#get length 

print(len(fruits))

#append to list - add to end 

fruits.append('grape')

#remove from list

print(fruits)

fruits.remove('grape')

print(fruits)

#insert into position

fruits.insert(1, "berry")

print(fruits)

#remove from position 
fruits.pop(1)

#reverse list

# fruits.reverse()

# sort - sorts alphabeticaly 

fruits.sort()

#sort - reverse 

fruits.sort(reverse=True)



print(fruits)

 



