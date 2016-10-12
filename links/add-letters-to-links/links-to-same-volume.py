import os
import re


def searchLetter(lNum, dirname):
	lName = dirname + '/' + 'letter' + lNum + '.xml'
	# print(lName)
	table = open('letters-list-short.csv', 'r', encoding='utf-8')
	lettersList = table.readlines()
	table.close()
	for line in lettersList:
		if lName in line:
			sepIndex = line.find(';')
			letterID = line[sepIndex+1:len(line)-1]
			normalName = dirname + '/' + letterID + '.xml'
			return normalName


def searchLink(lPath, dirname):
	lFile = open('.' + os.sep + lPath, 'r', encoding='utf-8')
	letter = lFile.readlines()
	ltext = lFile.read()
	regLink = re.compile('См\. письмо № ([1-9]?[0-9]?[0-9])\.')
	for line in letter:
		if re.search(regLink, line):
			# letterNum = regLink.group(1)
			res = re.search(regLink, line)
			letterNum = str(res.group(1))
			linkedLetter = searchLetter(letterNum, dirname)
			print(lPath+ ' - ' + res.group(0) + ' - ' + str(linkedLetter))
		
	

def main():
	for i in range(59,83):
		dirname = 'Volume_' + str(i)
		for letter in os.listdir(dirname):
			if letter.endswith('.xml'):
				searchLink(dirname + os.sep + letter, dirname)
		


if __name__ == '__main__':
	main()
