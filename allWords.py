def main():
	testString="yxmijcmknbshdwifzrsmueist"
	for line in open("enwordlist.txt"):
		w=True
		line=line.rstrip()
		for let in line:
			if let not in testString:
				w=False
				break
		if(w):
			print(line)


main()