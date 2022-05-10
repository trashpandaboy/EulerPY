from datetime import datetime

from reusable_functions import getAmountOfDivisors, getTriangleNumberOfNumber


start = datetime.now()

def main():

    divisorsAmount = 0
    number = 1
    lastNatural = 1
    while divisorsAmount < 500:
        naturalNumber = getTriangleNumberOfNumber(number)
        lastNatural = naturalNumber
        divisorsAmount = getAmountOfDivisors(naturalNumber)
        
        print("%s : %s"%(str(naturalNumber),str(divisorsAmount)))
        number += 1
    
    return lastNatural


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))