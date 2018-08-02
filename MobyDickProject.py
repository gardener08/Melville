# This is the Moby Dick program
import re

def readStopWordList():
	stopWordFile = open('StopWords.txt',encoding='utf-8')
	wordsToRemove = []
	for line in stopWordFile:
		lineForAnalysisWithoutNewline = line[:-1]
		lineForAnalysisWithoutNewlineOrWhitespace = lineForAnalysisWithoutNewline.rstrip()

		commentLineRegEx = r'^#'
		if lineForAnalysisWithoutNewlineOrWhitespace is '' or lineForAnalysisWithoutNewlineOrWhitespace is None or lineForAnalysisWithoutNewlineOrWhitespace is '\n':
			continue
		elif re.match(commentLineRegEx, lineForAnalysisWithoutNewlineOrWhitespace):
			continue
		else:
			wordsToRemove.append(lineForAnalysisWithoutNewlineOrWhitespace)
	return wordsToRemove

def setupWordDictionary():
	mobyDickTextFile = open('MobyDickInputFile.txt',encoding='utf-8')
	lineCount = 0
	wordDictionary = {}

	stopWordList = readStopWordList()
	#print(stopWordList)

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
			elif value not in stopWordList:
				if value in wordDictionary:
					wordDictionary[value] = wordDictionary[value] + 1
				else:
					wordDictionary[value] = 1
	return wordDictionary
				
def getWordsByCount(wordDictionary):
		
	wordsByCount = {}

	# value is the count	
	for wordKey in wordDictionary.keys():
		# is there a word with this particular count 
		currentWord = wordKey
		countOfCurrentWord = wordDictionary[wordKey]
		if countOfCurrentWord in wordsByCount:
			listOfWordsWithThisCount = wordsByCount[countOfCurrentWord]
			listOfWordsWithThisCount.append(currentWord)
		else:
			listOfWordsToCreateForThisCount = []
			listOfWordsToCreateForThisCount.append(currentWord)
			wordsByCount[countOfCurrentWord] = listOfWordsToCreateForThisCount
			
	return wordsByCount

def getTopTenWordCounts(wordsByCount):
	wordCounts = list(wordsByCount.keys())
	wordCounts.sort(reverse=True)

	topTenWordCounts = wordCounts[0:10]
	return topTenWordCounts
	
def outputResults(wordDictionary, wordsByCount, topTenWordCounts):
	
	print('Number of unique words in Moby Dick is: ' + str(len(wordDictionary)))

	print('Here are the top ten word counts with their words')
	for wordCount in topTenWordCounts:
		wordsForThisCount = wordsByCount[wordCount]
		wordsForThisCountStr = ''
		for word in wordsForThisCount:
			wordsForThisCountStr += word + ','
		# Remove the trailing comma
		wordsForThisCountStr = wordsForThisCountStr[:-1]
		print(str(wordCount) + ': ' + wordsForThisCountStr)

wordDictionary = setupWordDictionary()
wordsByCount = getWordsByCount(wordDictionary)
topTenWordsByCount = getTopTenWordCounts(wordsByCount)
outputResults(wordDictionary, wordsByCount, topTenWordsByCount)
