string = input("Enter sentence to encrypt: ")
shift = int(input("Enter value to shift characters by: "))

stringl = string.split()
wordList = []
i = 0
for word in stringl:
	wordList.append([])
	for letter in word:
		x = ord(letter)
		if x in range(97, 123):
			x += shift
			if x > 122:
				x = 96 + (x - 122)
		elif x in range(65, 91):
			x += shift
			if x > 90:
				x = 64 + (x - 90)
		
		wordList[i].append(chr(x))
	i += 1
		
print(wordList)
for word in wordList:
	for letter in word:
		print(letter.strip(), end = "")
	print(" ", end = "")
print()