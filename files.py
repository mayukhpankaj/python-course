# python has functions for creating & writing files

#open a file

myFile = open('file.txt','w')


#get info

print('name: ', myFile.name)
print('is_close ', myFile.closed)
print('opening mode',myFile.mode)

#write to file

myFile.write('I love python')

myFile.close()

# append to a file

# myFile = open('file.txt','a')
# myFile.write(' end ! ')


#read from file

myFile = open('file.txt', 'r')

text = myFile.read(100)

print(text)
