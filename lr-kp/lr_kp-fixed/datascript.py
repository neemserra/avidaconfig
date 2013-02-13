#This is a program to parse a data file that was created with Avida's analyze
#mode. The analyze file had a line with the name of the file followed by a line 
#with data from the DETAIL function in analyze mode.  This script parses the file
#based on a variable, and it allows for extraction of data (file name & genotype)
#for runs that have a certain value.

fd = open("neemdata", "r") #open datafile in read mode
output = open("instructionoutput", "w") #makes a new file (neemoutput) set to write
readthings = fd.readlines() #reads the lines in a file
myList = [] #blank list

for line in readthings: 
	linestrip = line.strip()
	#print linestrip
	if len(linestrip) < 1:
		continue
	linesplit = linestrip.split()
	#print linesplit
	#goes through line by line, strips it of end characters, takes away lines
	#that do not have anything in them, then it splits the line on spaces and
	#inputs the data into a list
	
	if linesplit[0] == '==>':
		myList.append(linesplit[1])
		#print myList
		#Every other line is a list that has the file name in position 1, and is
		#flanked by '==>' and '<==' in the list.  This takes the file name and 
		#appends it to a list
	if linesplit[0] == '1':
		myList.append(linesplit[2])
		#print myList
		#print len(myList)
		outputString = myList[0] + " " + myList[1] + "\n"
		output.write(outputString)
		myList = []
		#if it has the instruction, it reads as 1, and those are the ones I want
		#it will add the genome to the list with the file name, and then it will
		#write that one one line to a new file
	if linesplit[0] == '0':
		myList = []
		#if it does not have the instruction, it will clear the list of the file
		#name and move on
		
output.close()
