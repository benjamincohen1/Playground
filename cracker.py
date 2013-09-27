import crypt, re

def test(password):
	salt = password[0:2]
	dictionary = open("wordsEn.txt")
	for word in dictionary:
		word = re.sub("\n","",word)
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == password:
			return "Pass is: " + str(word)
	return "Not Found"
if __name__ == "__main__":
	passFile = open('passes.txt')
	for line in passFile:
		if ':' in line:
			user, passwd = line.split(":")[0], line.split(":")[1]
			passwd = passwd.strip()
			print "Cracking password for user: "+str(user)
			print test(passwd)