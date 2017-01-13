#Exercise 2 page 89
 
file_name = raw_input("Enter a file name: ") # Enter a file name

file_open = open(file_name)

count = 0

for line in file_open:	

	if line == ("X-DSPAM-CONFIDENCE:0.8475"):
		
		count +=1
		
print count
	
print (line)

	

