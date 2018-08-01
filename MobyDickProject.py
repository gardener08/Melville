# This is the Moby Dick program
mobyDickTextFile = open('MobyDickInputFile.txt',encoding='utf-8')
lineCount = 0
for line in mobyDickTextFile:
	lineCount = lineCount + 1
print(lineCount)

