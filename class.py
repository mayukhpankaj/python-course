# A class is a blueprint for creating object 
# object has properties and functions in it

# creating class 


class user: 
    #constructor 

    def __init__(self,name,age,email):
        
        self.nm = name 
        self.email = email
        self.yr = age 

    def greeting(self):
        return f'Hello {self.nm}'

    def has_birthday(self):
         self.yr+=1


# creating object 

obj = user('mayukh',20,'may@gmail.com') 

print(obj.yr)

print(obj.greeting())

obj.has_birthday()

print(obj.yr)


""" Extending class """

class customer(user):

    #constructor 
    def __init__(self, name, age, email ):
        self.balance=0 
        self.name = name
        self.yr = age
        self.email = email

    def set_balance(self,money):
        self.balance= money

trips = customer('trip', 18, 'trip@hotmail.com')

# print(trips.greeting())

trips.set_balance(1000000)

print(trips.balance)




