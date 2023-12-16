def NULL_not_found(object: any) -> int:
	if (object == None):
		print("Nothing:", object, type(object))
	elif (isNaN(object)):
		print("Cheese:", object, type(object))
	elif (object == 0):
		print("Zero:", object, type(object))
	elif (object == ""):
		print("Empty:", type(object))
	elif (object == False):
		print("Fake:", object, type(object))
	else:
		print("Type not Found")
		return 1
	return 0

def isNaN(num):
	return num != num
