""" 
A set is a collection which is unordered and unindexed 
NO DUPLICATE MEMBERS
"""

# create set 

fruit = {'apple','orange','mango'}

print(fruit,type(fruit))

#check if in set 

print('apple' in fruit) # True 

#add to set

fruit.add('grape')

#remove 

fruit.remove('grape')

#clear set 
# fruit.clear()

#delete 
# del fruit

fruit.add('apple')   #apple already in set , no error. 

print(fruit)