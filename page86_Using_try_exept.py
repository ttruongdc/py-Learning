#Page 86 
#Using try and except commands to run when users enter wrong data type.

fname = raw_input("Enter file name: ") # Asking user to input a file


try:	
	fhand = open(fname) # Open the file using open module
	
except:

	print('File cannot be opened.', fname)
	
	exit()
	
	
count = 0  #Initializing variable 'count'.

for line in fhand:
	
	if line.startswith('Subject:'):
		
		count = count + 1
		
print ('There were %d "subject line" in %s') % (count, fname)