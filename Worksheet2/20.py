queenList = []

def checkCol(col, queenList):
	for i in queenList:
		if i[1] == col:
			return False
			
	return True

def checkDiag1(row, col, queenList):
	sum_put = row + col
	for i in queenList:
		sum_chk = i[0] + i[1]
		if sum_chk == sum_put:
			return False
			
	return True
	
def checkDiag2(row, col, queenList):
	dif_put = row - col
	for i in queenList:
		dif_chk = i[0] - i[1]
		if dif_chk == dif_put:
			return False
			
	return True
	
def placeQueen(queenList, row, queens):
	if row == queens:
		return True
	
	for col in range(queens):
		if (checkCol(col, queenList) and checkDiag1(row, col, queenList) and checkDiag2(row, col, queenList)):
			queenList.append((row, col))
			if placeQueen(queenList, row+1, queens):
				return True
			else:
				queenList.remove(queenList[-1])
				continue
				
	return False
			
	
if placeQueen(queenList, 0, 8):
	print(queenList)
else:
	print(False)