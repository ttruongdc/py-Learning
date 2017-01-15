#Using built-in functions to compute average.

numlist = list() # Initialize 'numlist' = a list of number.

while (True):	# If value stays True, program keeps running.
	
	inp = raw_input("Enter a number:") #Get user input value
	
	if inp == 'done': # break program when user is finish entering numbers
		break
	
	
	value = float(inp) # change string to float type and assign to 'value' variable
	
	numlist.append(value)  #Using 'append' method to add item to the list 'numlist'.
	
average = sum(numlist) / len(numlist)  #Compute average using built-in functions sum and len
print numlist # Showing list of numbers entered by user on screen
print ("Average is %f") % average #print output to screen.
	


