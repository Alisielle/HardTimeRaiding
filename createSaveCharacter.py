def save(*characters):
	save = open("save.csv","w")
	s = ""

	for c in characters:s +=  repr(c)+"\n"
	
	save.write(s)
	save.close