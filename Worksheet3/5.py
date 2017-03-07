import re
f = open("romeo.txt" , "r")

wordsDict = {}
for line in f:
	line = line.lower().split()
	for word in line:
		if word.isalpha() == False:
			word = re.sub(r'\W+', '', word)
		
		if word in wordsDict:
			wordsDict[word] += 1
		else:
			wordsDict.setdefault(word, 1)
			
f.close()

f = open("R_&_J_Word_Frequencies.txt", "w")

for i in wordsDict:
	if i.isalpha():
		line  = i + ", " + str(wordsDict[i]) + "\n"
		f.write(line)
	
f.close()