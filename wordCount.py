import re #Regular Expression Tools
import sys #Use command line arguments

inputFile = sys.argv[1]

outputFile = sys.argv[2]

file2 = open(outputFile,"w")

with open(inputFile, 'r') as f:
    for line in f:
        for word in line.split():
            if True:
                file2.write(word)
                print(word)


file2.close()


