string = input("Enter a string: ")

def rev(strin, strout):
	if len(strin) == 0:
		return strout
	
	strout = strout + strin[-1]
	strin = strin[:-1]
	
	return rev(strin, strout)
	
print(rev(string, ""))