from datetime import datetime

start = datetime.now()

def main():
    maxNumber = 1000
    multiplesOfThreeOrFive = []

    multiplierForThree = 1
    multipleOfThree = 0

    while multipleOfThree < maxNumber:
        multipleOfThree = 3 * multiplierForThree
        if(multipleOfThree < maxNumber):
            if multipleOfThree not in multiplesOfThreeOrFive:
                multiplesOfThreeOrFive.append(multipleOfThree)
        multiplierForThree += 1

    
    multiplierForFive = 1
    multipleOfFive = 0
    while multipleOfFive < maxNumber:
        multipleOfFive = 5 * multiplierForFive
        if(multipleOfFive < maxNumber):
            if multipleOfFive not in multiplesOfThreeOrFive:
                multiplesOfThreeOrFive.append(multipleOfFive)   
        multiplierForFive += 1

    return sum(multiplesOfThreeOrFive)
    

value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))