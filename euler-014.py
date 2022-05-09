from datetime import datetime

from reusable_functions import collatzSequence

start = datetime.now()

def main():

    highestStartingNumber = 1
    sequenceLenght = 1
    number = 1
    targetNumber = 999999
    while number < targetNumber:
        result = collatzSequence(number)
        if(len(result) > sequenceLenght):
            highestStartingNumber = number
            sequenceLenght = len(result)
        number += 1

    return highestStartingNumber


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))