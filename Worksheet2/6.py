l = [5, 124, 000, 234]

def mean(l):
	added = 0
	for i in l:
		added += i
	
	return added / len(l)
	
print(mean(l))