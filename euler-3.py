
from datetime import datetime
import string
import random
import json
import sys


number = 13195

if(len(sys.argv) > 1):
    number = int(sys.argv[1])
    if number < 3:
        number = 3
    print("number set to %s"%number)

start = datetime.now()

def isPrime(number):
    if number > 1:
    # check for factors
        i = 2
        while i < number:
            if (number % i) == 0:
                return False
            i+= 1
        
        return True

def largestFactor(number):
    
    divider = number / 2
    while(divider > 1):
        if(number%divider == 0):
            if(isPrime(divider)):
                return divider
        divider -= 1

    return 1

print(largestFactor(number))

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))