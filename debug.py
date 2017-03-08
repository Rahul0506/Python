def checkHorWin(colIn, movesDict, k, playerMarker):
	print("Checking Hor victory...")
	checkInd = movesDict[colIn].index(movesDict[colIn][-1])		#Index of the last played move in its column's string
	checked = 0		#No. of positions checked
	win = False
	
	for i in range(1,k):		#Iterate for columns to check
		if checked >= (k - 1):		#If the no. of positions checked if k-1, return win as true. BUT IT DOESNT WORK!
			win = True
			print(win)
			break
		else:
			try:
				x = movesDict[colIn+i][checkInd]		#Check if column exists, then if index exists
				print("checking to right")
				print(x, " ", playerMarker)
			except:
				win = False
				break
			else:
				if x == playerMarker:		#If value in column and index is same, increase checked columns
					checked += 1
					print(checked)
				else:
					win = False		#If the value in column and index is not the same , stop iterating and return win as false
					break
					
	return win
	
dict = {1 : "X", 2 : "X", 3 : "X", 4 : "X"}		#Simulation of a win
win = checkHorWin(1, dict, 4, "X")
print(win)