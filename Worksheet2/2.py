num = int(input("Enter a positive integer: "))

def printWord(num):
	list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	
	for i in str(num):
		print(list[int(i)], end = " ")
	print()
	
printWord(num)