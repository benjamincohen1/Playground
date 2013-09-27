import math, re


def getAutoComplete(inputString):
	inputString = inputString.lower()
	numSuffixes = ["th", "st", "nd",' "rd']

	inputString = inputString.strip(".")
	for suffix in numSuffixes:
		inputString = re.sub(r"(\d+)"+suffix,r'\1', inputString)

	words = {"first": 1, "second": 2, "third": 3, 
			 "fourth": 4, "fifth": 5, "sixth": 6,
			 "seventh": 7, "eighth": 8, "ninth": 9}

	for key in words.keys():
		inputString = re.sub(str(key), str(words[key]), inputString)

	abbreviations = {"av": "avenue", "ave": "avenue", "st": "street",
					 "str": "street", "rd": "road", "roa": "road", "blvd": "boulevard"}

	for key in abbreviations.keys():
		inputString = re.sub(" "+str(key)+" ", " "+str(abbreviations[key])+" ", inputString)

	directions = {"n": "north", "w": "west", "s": "south", "e": "east"}

	for key in directions.keys():
		inputString = re.sub(" "+str(key)+" ", " "+str(directions[key])+" ", inputString)

	units = [
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
		"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
		"sixteen", "seventeen", "eighteen", "nineteen",
	  ]

	tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	scales = ["hundred", "thousand", "million", "billion", "trillion"]
	if re.match("\d",inputString[0]) is None:
		numberWords = []
		for word in inputString.split():
			if word not in units and word not in tens and word not in scales:
				break
			else:
				numberWords.append(word)
		
		s = ""
		for word in numberWords:
			s += word+" "

		inputString = re.sub(str(s),str(text2int(s)) + " ", inputString)



	return inputString


def text2int(textnum, numwords={}):
	if not numwords:
	  units = [
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
		"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
		"sixteen", "seventeen", "eighteen", "nineteen",
	  ]

	  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	  scales = ["hundred", "thousand", "million", "billion", "trillion"]

	  numwords["and"] = (1, 0)
	  for idx, word in enumerate(units):    numwords[word] = (1, idx)
	  for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
	  for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

	current = result = 0
	for word in textnum.split():
		if word not in numwords:
		  raise Exception("Illegal word: " + word)

		scale, increment = numwords[word]
		current = current * scale + increment
		if scale > 100:
			result += current
			current = 0

	return result + current


if __name__ == "__main__":
	tests = ["101 8th avenue",
			 "200 fifth st.", 
			 "one hundred 7 avenue",
			 "one hundred eight seventh avenue",
			 "100 7th avenue",
			 "10 avenue of the americas",
			 "8 broadway",
			 "100 west broadway",
			 "one hundred west broadway",
			 "100 w broadway",
			 "100 w. broadway",
			 "100 w bdwy",
			 "8-10 w 19th",
			 "empire state building",
			 "madison square garden",
			 "10 avenue of americas",
			 "1 1st street",
			 "2 second st",
			 "2 2nd st",
			 "one first street"]

	for t in tests:
		print "Test String: "+str(t)
		print "Returned String: "+str(getAutoComplete(t))
		print ""