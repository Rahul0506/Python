l = [99.239817, 23783, 8479, 238, 773783.1862, 24846, 0000.0000]

def lowest(l):
	lowest = 0
	for i in l:
		if i < lowest:
			lowest = i
			
	return lowest

print(lowest(l))