import re
def main():
	words = []
	for line in open("wordsEn.txt"):
		words.append(line.replace("\n",""))
	pattern = ""
	parts = []
	for line in open("parts"):
		parts.append(line.replace("\n",""))

	for x in words:
		for y in parts:
			pattern=y+"\w\w\w"
			#print(pattern)
			m = re.match(x,pattern)
			if m:
				print m.group()

main()