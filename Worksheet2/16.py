stackSize = int(input("Enter number of disks: "))

def hanoi(disks, start, end, temp):
	if disks <= 0:
		pass
	else:
		for step in hanoi(disks - 1, start, temp, end):
			yield step
		yield(start, end)
		for step in hanoi(disks - 1, temp, end, start):
			yield step
		
print([step for step in hanoi(stackSize, 1, 3, 2)])