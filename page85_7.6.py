fname = raw_input('Enter a file name:')
fhand = open(fname)

count = 0
for line in fhand:
	if line.startswith('Subject'):
		count +=1
print ("There were %d 'subject lines in' %s.") % (count, fname)
