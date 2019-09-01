import re #Regular Expression Tools
import sys #Use command line arguments

inputFile = sys.argv[1]
outputFile = sys.argv[2]

count = 0

file = open(inputFile).read().lower()
file2 = open(outputFile,'w')
newString = re.sub('[^a-zA-Z0-9]',' ',file)
sortedNewString = newString.split()
sortedNewString.sort()

oneDicto = {}
#print(sortedNewString)

for word in sortedNewString:
        if word in oneDicto.keys():
                oneDicto[word] = oneDicto[word] + 1
        else:
                oneDicto[word] = 1

for word in oneDicto.keys():
        file2.write(word+" "+str(oneDicto[word])+"\n")
        

file2.close()


