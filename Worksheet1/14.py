num = input("Enter your number: ")
sigReq = int(input("Enter number of significant figures required: "))

numList = num.split(".")
if numList[0][0] == "-":
	print("-", end = "")
	numList[0] = numList[0][1:]
	
numList[0] = str(int(numList[0]))

for i in range(sigReq):
	try:
		print(numList[0][i], end = "")
	except:
		break
sigReq -= len(numList[0])

if sigReq > 0:
	print("." , end = "")
	try:
		string = numList[1]
	except:
		pass
	else:
		for i in range(sigReq):
			try:
				print(numList[1][i], end = "")
			except:
				break
		sigReq -= len(numList[1])
		
if sigReq > 0:
	for i in range(sigReq):
		print("0", end = "")
		
print()