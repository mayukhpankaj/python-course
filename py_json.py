#API use json to exchange data 

import json

userJSON = '{"firstname":"john","age":30}'

# json to dict - parse to Dict 

data = json.loads(userJSON)

print(data['age'])

print(type(data))


#dict to JSON - parse to JSON 

car = {'make':'ford','model':'GT40'}

print(type(data))

carJSON = json.dumps(car)

print(type(carJSON))

