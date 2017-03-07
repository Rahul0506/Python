f = open("iris.data", "r")

content = []
i = 0

for line in f:
	content.append(line.strip().split(","))

print(content)
f.close()