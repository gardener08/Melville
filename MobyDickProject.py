# This is the Moby Dick program
import re
from tkinter import *

# tkinter code partially based on a tutorial at: https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# I also used other search engine results as references for this work.
# I used Learning Python by Mark Lutz and Regular Expression Pocket Reference by Tony Stubblebine as references as well.

class MobyDickBusinessLogic:

	def readStopWordList(self):
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
				wordsToRemove.append(lineForAnalysisWithoutNewlineOrWhitespace.lower())
		return wordsToRemove

	def setupWordDictionary(self):
		mobyDickTextFile = open('MobyDickInputFile.txt',encoding='utf-8')
		lineCount = 0
		wordDictionary = {}

		stopWordList = self.readStopWordList()
		#print(stopWordList)

		for line in mobyDickTextFile:
			lineCount = lineCount + 1
			lineForAnalysis = str(line)
			lineForAnalysisWithoutNewline = lineForAnalysis[:-1]
			#print(lineForAnalysisWithoutNewline + '###')
			regEx = r'[^a-zA-Z_]'
			lineForAnalysisWithoutNewlineOrWhitespace = lineForAnalysisWithoutNewline.rstrip()
			lineForAnalysisWithoutNewlineOrWhitespaceLowerCase = lineForAnalysisWithoutNewlineOrWhitespace.lower()
			brokenUpLine = re.split(regEx, lineForAnalysisWithoutNewlineOrWhitespaceLowerCase)
			
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
					
	def getWordsByCount(self,wordDictionary):
			
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

	def getTopTenWordCounts(self,wordsByCount):
		wordCounts = list(wordsByCount.keys())
		wordCounts.sort(reverse=True)

		topTenWordCounts = wordCounts[0:10]
		return topTenWordCounts
		
	def outputResults(self,wordDictionary, wordsByCount, topTenWordCounts):
		
		#print('Number of unique words in Moby Dick is: ' + str(len(wordDictionary)))
		resultsString = 'Number of unique words in Moby Dick is: ' + str(len(wordDictionary)) + '\n'
		#print('Here are the top ten word counts with their words')
		resultsString += 'Here are the top ten word counts with their words.  The search and results are not case sensitive.\n'
		resultsString += 'A standardized list of common words is filtered out of the results.\n'
		for wordCount in topTenWordCounts:
			wordsForThisCount = wordsByCount[wordCount]
			wordsForThisCountStr = ''
			for word in wordsForThisCount:
				wordsForThisCountStr += word + ','
			# Remove the trailing comma
			wordsForThisCountStr = wordsForThisCountStr[:-1]
			#print(str(wordCount) + ': ' + wordsForThisCountStr)
			resultsString += str(wordCount) + ': ' + wordsForThisCountStr + '\n'

		return resultsString
			
	def runBusinessLogic(self):
		wordDictionary = self.setupWordDictionary()
		wordsByCount = self.getWordsByCount(wordDictionary)
		topTenWordsByCount = self.getTopTenWordCounts(wordsByCount)
		results = self.outputResults(wordDictionary, wordsByCount, topTenWordsByCount)
		return results

class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)               
		self.master = master
		
	def initWindow(self):
		self.master.title("Moby Dick")
		self.pack(fill=BOTH, expand=1)
		self.master.geometry('650x500')
		
		get10MostPrevalentWordsButton = Button(self, text='Get 10 most common words in Moby Dick', command=lambda: self.outputResults())
		get10MostPrevalentWordsButton.place(x=0, y=0)
		get10MostPrevalentWordsButton.pack()
		#get10MostPrevalentWordsButton.pack(padx=5, pady=5, side=LEFT)

		self.master.topTenText = Text(self.master, height=30, width=80)
		self.master.topTenText.pack()
		
	def outputResults(self):
		businessLogic = MobyDickBusinessLogic()
		topTenList = businessLogic.runBusinessLogic()
		self.master.topTenText.insert(END, topTenList)
		
		
root = Tk()		
app = Window(root)
app.initWindow()
root.mainloop()

