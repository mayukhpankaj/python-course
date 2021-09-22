# a block of code which runs when called. 
# in python we don use curly braces. 
# we use identation with tabs or spaces 


""" create function """

def say():
    print('hello world')

say()

print(type(say))

""" function with argument """

# def  sayHello(name='john doe'):
#     print(f'Hello {name}')
    
# sayHello('may')


""" Return values """


# def getsum(num1, num2):
#     total = num1 + num2
#     return total

# print(getsum(3, 4))

""" lamda function is an anonymous function.
    can take multiple arguements
    BUT only one EXPRESSION.
    similar to arrow fn in JS
 """

getSum = lambda num1, num2: num1 + num2

print(getSum(10,2))







