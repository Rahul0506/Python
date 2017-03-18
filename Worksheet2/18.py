l = [1, 2, 3]

def power_set(l):
	result = [[]]
	for i in l:
		newset = [x + [i] for x in result]
		result.extend(newset)
	
	return result
	
print(power_set(l))