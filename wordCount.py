import re #Regular Expression Tools
import sys #Use command line arguments

inputFile = sys.argv[1]
outputFile = sys.argv[2]

file = open(inputFile).read().lower() #Open and read the file in lowercase
file2 = open(outputFile,'w') #Open the file and be ready to write
newString = re.sub('[^a-zA-Z0-9]',' ',file) #Ignore anything that is not a letter or number
sortedNewString = newString.split() #Spliting the word into a list
sortedNewString.sort() #Sorting the list in alphabetical order

oneDicto = {} #Creating a Dictionary

"""
In this for loop, it's just couting the instances of every word
and add the a plus one. 
"""
for word in sortedNewString: 
        if word in oneDicto.keys():
                oneDicto[word] = oneDicto[word] + 1
        else:
                oneDicto[word] = 1

for word in oneDicto.keys():
        file2.write(word+" "+str(oneDicto[word])+"\n") #Writing into the new file
        

file2.close() #close the file


