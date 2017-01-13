
def compute(x,y): # Initializing a function to compute average

	average = sum / count # Average = total divide for number of counts 
	return ("The total is: %f , the count is: %d and the average is: %f") % (sum, count, average)	# Return a value of total, count and average

count = 0 # Initialize count = 0
sum = 0 # Initialize and assign value to variable 'sum' = 0

while True: # loop

	num = eval(raw_input("Enter a number: ")) # Get input number
	
	if num >0:
	
		sum = sum + num # Keep adding the number to total

		count += 1 # Tallying how many times the loop execute.

	if len(num) == 0:
		break

print compute(sum, count)# Calling function "compute"

	# Print "return from function" to screen. 

	#print "Oop!  Please Enter number:"