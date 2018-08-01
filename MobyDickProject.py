# This is the Moby Dick program
import re
mobyDickTextFile = open('MobyDickInputFile.txt',encoding='utf-8')
lineCount = 0
wordDictionary = {}
for line in mobyDickTextFile:
	lineCount = lineCount + 1
	lineForAnalysis = str(line)
	lineForAnalysisWithoutNewline = lineForAnalysis[:-1]
	#print(lineForAnalysisWithoutNewline + '###')
	regEx = r'[^a-zA-Z_]'
	lineForAnalysisWithoutNewlineOrWhitespace = lineForAnalysisWithoutNewline.rstrip()
	brokenUpLine = re.split(regEx, lineForAnalysisWithoutNewlineOrWhitespace)
	
	#print('line: ' + lineForAnalysisWithoutNewlineOrWhitespace + '###')
	#print(brokenUpLine)
	for value in brokenUpLine:
		if value == '' or value is None or value is '\n':
			continue
		elif value in wordDictionary:
			wordDictionary[value] = wordDictionary[value] + 1
		else:
			wordDictionary[value] = 1

superKeyList = []
wordDictionaryKeys = wordDictionary.keys()
for key in wordDictionaryKeys:
	superKeyList.append(str(wordDictionary[key]) + ':' + key)

print('Number of words in Moby Dick is: ' + str(len(wordDictionary)))
print('Number of words in superKeyList is: ' + str(len(superKeyList)))

# The sort function doesn't return anything but sorts the list it is given.
superKeyListSorted = superKeyList
superKeyListSorted.sort(key=str.lower)

topTenWords = superKeyListSorted[0:10]
for word in topTenWords:
	wordCombo = re.split(':',word)
	wordValue = wordCombo[1]
	wordCount = wordCombo[0]
	
	print('Word ' + wordValue + ' appears ' + str(wordCount) + ' times.')

print('Least prevalent word: ' + superKeyListSorted[0])

print('Most prevalent word: ' + superKeyListSorted[18921])

	





