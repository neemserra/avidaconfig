#This is a program to parse a data file that was created with Avida's analyze
#mode. The analyze file had a line with the name of the file followed by a line 
#with data from the DETAIL function in analyze mode.  This script parses the file
#based on a variable, and it allows for extraction of data (file name & genotype)
#for runs that have a certain value.

fd = open("neemdata", "r") #open datafile in read mode
output = open("neemoutput", "w") #makes a new file (neemoutput) set to write
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

fdAnalyze = open("neemoutput", "r") #open Avida datafile in read mode
fdPython = open("hdiv3data", "r") #opens Python datafile
output2 = open("neemoutputcombined", "w") #makes a new file set to write
readthingsA = fdAnalyze.readlines() #reads the lines in a file
readthingsP = fdPython.readlines()
newline = ""
datahDiv = []
analyzeData = []

for line in readthingsP:
	linestrip = line.strip()
	#print linestrip
	if len(linestrip) < 1:
		continue
	linesplit = linestrip.split()
	#print linesplit
	#goes through line by line, strips it of end characters, takes away lines
	#that do not have anything in them, then it splits the line on spaces and
	#inputs the data into a list
	
	full_run_name = linesplit[0]
	#print full_run_name
	run_name = full_run_name[7:]
	#print run_name
	#.strip deletes part of a string object and takes out all instances of
	#that character.  instead we found the 14th character and took the file name
	#past that number character
	hData = linesplit[1:]
	#get all the things in the list except for the file name
	hData.insert(0, run_name)
	#now insert the truncated file name in front of the list
	datahDiv.append(hData)
	
#print datahDiv

for lineA in readthingsA:
	linestripA = lineA.strip()
	if len(linestripA) <1:
		continue
	linesplitA = linestripA.split()
	#print linesplitA
	full_run_name_analyze = linesplitA[0]
	#print full_run_name_analyze
	run_name2 = full_run_name_analyze[45:-4]
	#print run_name2
	aData = []
	aData.append(linesplitA[1])
	#takes the genome line and adds it to a list
	aData.insert(0, run_name2)
	#adds the truncated file name line in front of the genome
	analyzeData.append(aData)

#print analyzeData
combinedData = []	
for list in analyzeData:
	for list2 in datahDiv:
		if list[0] == list2[0]:
			list2.append(list[1])
			combinedData.append(list2)
#take the first list and compare it with the second list by seeing if the first
#thing in each list (the file name) is the same.  If it is the same, append the
#genome to the list

print combinedData

for listItem in combinedData:
	writeString = ""
	for item in listItem:
		writeString = writeString + " " + item
		print writeString
	writeString = writeString + "\n"
	output2.write(writeString)
#this is the function to write the data to a file.  you can't write a list to a 
#file so we are iterating through the list and adding spaces between things, and 
#after each list of data (from one run), we add a new line to separate the data s

output2.close()