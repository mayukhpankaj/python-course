# A for loop is used for iterating over a sequence: 
# like for List , tuple , dictionary , set , string ! 

# simple loop

# for num in range(10):
#     print(num)


people = ['john','may','sara']

# ctr =1

# for person in people:
#     print(ctr,person)
#     ctr=ctr+1


""" break """

# for person in people:

#     if person == 'sara':
#         break
#     print(person)

""" contine """

# for person in people:

#     if person == 'may':      
#         continue            #skips may 
#     print(person)

for i in range(len(people)):
    print(people[i])


""" while loop """

#executes block of statements as lon as condition is true 

# count = 0

# while count <=10:
#      print(count)
#      count +=1 
