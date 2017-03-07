from random import randint
name = ""
for i in range(100):
	name = name + str(randint(0, 9))
	
name = name + ".txt"

try:
	f = open(name, "r")
except:
	print("No such file exists!")
else:
	data = f.read()
	f.close()