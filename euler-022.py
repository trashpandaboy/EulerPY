from datetime import datetime

from reusable_functions import getStringValue

start = datetime.now()

def main():
    namesFile = open("files/p022_names.txt")
    names = namesFile.read().split(',') #spli the first line with comma separator
    names.sort() #use sort function to achieve alphabetical order
    
    scores = [] #create a scorelist
    position = 0
    for name in names:
        position += 1
        scores.append(getStringValue(name.strip('"')) * position) #get the string value and multiply it by the position in alphabetical list

    return sum(scores)


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))

