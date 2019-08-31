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

print(sortedNewString)
for line in sortedNewString:
    for word in line.splitlines():    
        #if word not in file2.read():
            print(line)
            count = file.count(word)
            print(count)
            file2.write(line+" "+str(count)+"\n")

file2.close()


