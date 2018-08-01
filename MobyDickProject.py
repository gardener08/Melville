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
	regEx = r'[\W]'
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
			wordDictionary[value] = 0

superKeyList = []
wordDictionaryKeys = wordDictionary.keys()
for key in wordDictionaryKeys:
	superKeyList.append(str(wordDictionary[key]) + ':' + key)

print('Number of words in Moby Dick is: ' + str(len(wordDictionary)))
print('Number of words in superKeyList is: ' + str(len(superKeyList)))
print('Example SuperKey: ' + superKeyList[10])
print('Example SuperKey: ' + superKeyList[20])
print('Example SuperKey: ' + superKeyList[30])
print('Example SuperKey: ' + superKeyList[40])
print('Example SuperKey: ' + superKeyList[50])
print('Example SuperKey: ' + superKeyList[60])




