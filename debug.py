def checkHorWin(colIn, movesDict, k, playerMarker):
	print("Checking Hor victory...")
	checkInd = movesDict[colIn].index(movesDict[colIn][-1])
	checked = 0
	win = False
	
	for i in range(1,k):
		if checked >= (k - 1):
			win = True
			print(win)
			break
		else:
			try:
				x = movesDict[colIn+i][checkInd]
				print("checking to right")
				print(x, " ", playerMarker)
			except:
				win = False
				break
			else:
				if x == playerMarker:
					checked += 1
					print(checked)
				else:
					win = False
					break
					
	return win
	
dict = {1 : "X", 2 : "X", 3 : "X", 4 : "X"}
win = checkHorWin(1, dict, 4, "X")
print(win)