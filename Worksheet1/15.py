quant = int(input("Input a quantity: "))
quantType = input("Input type (length, area or volume): ")
baseIn = input("Select base unit of measurement (mm, cm, m or km): ")
baseOut = input("Select base unit to convert to (mm, cm, m or km): ")
suffix = ""

if quantType.lower() == "area":
	suffix = 2
elif quantType.lower() == "volume":
	suffix = 3

print(str(quant) + " " + baseIn + "^" + str(suffix) + " =", end = " ") 
	
baseDictOut = {"mm" : 1000, "cm" : 100, "m" : 1, "km" : 0.001}
baseDictIn = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000}

if baseOut != baseIn:
	quant *= (baseDictIn[baseIn] ** suffix)
	quant *= (baseDictOut[baseOut] ** suffix)
	
print(str(quant) + " " + baseOut + "^" + str(suffix))