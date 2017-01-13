#Reading a file
from sys import argv

fhand = open('test.txt')
print fhand.read()
count = 0
for line in fhand:
	count += 1
	
print ("Line count :" , count)
