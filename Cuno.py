
def compute(x,y): # Initializing a function to compute average

	average = x / y # Average = total divide for number of counts
	return ("The total is: %f , the count is: %d and the average is: %f") % (sum, count, average)	# Return a value of total, count and average

count = 0 # Initialize count = 0

sum = 0 # Initialize and assign value to variable 'sum' 	

while True:	
	try:  #Using try and except to handle strings entered by user

		while True: # loop
				
				num = raw_input("Enter a number: ")# Get input number
				
				if num == 'done':
				
					break
				
				if num.startswith(' '):
					
					continue
					
				num = float(num)
				
				if num >0:

					sum = sum + num # Keep adding the number to total
					count += 1 # Tallying how many times the loop execute.			
				
	except:
			
			print "What happened? You are supposed to enter numeric data only"
			
	confirm = input("Are you sure?  Enter yes to finish or no to go back.")
	print type(confirm)
	if confirm == ('yes'):
		break

	if confirm ==  ('no'):
		continue
   
print compute(sum, count)# Calling function "compute"

	