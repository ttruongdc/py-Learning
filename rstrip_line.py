fhand = open("mbox_short.txt")
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'):
		continue
		
	print (line)
