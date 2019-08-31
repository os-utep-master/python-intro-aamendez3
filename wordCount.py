import re #Regular Expression Tools
import sys #Use command line arguments

def check(word,file):
    newFile = open(file).read()
    if re.match(word,newFile):
        return False
    else:
        return True

inputFile = sys.argv[1]
outputFile = sys.argv[2]

count = 0

file = open(inputFile).read()
file2 = open(outputFile,"w")

print(file)
for line in file.split():
    print(line)
    for word in line.splitlines():    
        #if check(word,file2):
            print(line)
            count = file.count(word)
            print(count)
            file2.write(line+" "+str(count))

#with open('words.txt','r') as f:
 #   for line in f:
  #      for word in line.split():
   #        print(word)      
file2.close()


