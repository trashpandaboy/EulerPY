from reusable_functions import isPrime, listOfFirst10KPrimes
from datetime import datetime
import sys


number = 13195

if(len(sys.argv) > 1):
    number = int(sys.argv[1])
    if number < 3:
        number = 3
    print("number set to %s"%number)

start = datetime.now()

def largestFactor(number):
    listOfPrimes = listOfFirst10KPrimes()
    listOfPrimes = list(reversed(listOfPrimes))

    for prime in listOfPrimes:
        if(number % prime == 0):
            return prime
    return 1
    
    # divider = number / 2
    # while(divider > 1):
    #     print(divider)
    #     if(number%divider == 0):
    #         if(isPrime(divider)):
    #             return divider
    #     divider -= 1

    return 1

print(largestFactor(number))

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))