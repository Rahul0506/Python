f = open("WORDS.txt", "r")
data = f.read().split()
f.close()

wordList = []
freqList = []
for i in data:
	try:
		freq = int(i)
	except:
		wordList.append(i)
	else:
		freqList.append(freq)
		
indexOut = freqList.index(max(freqList))
print("First term with highest frequency is: " + wordList[indexOut])
print("With a frequency of: ", freqList[indexOut])