from reusable_functions import stringIsPalindrome
from datetime import datetime
import sys

number = 13195

if(len(sys.argv) > 1):
    number = int(sys.argv[1])
    if number < 3:
        number = 3
    print("number set to %s"%number)

start = datetime.now()

def biggestPalindromeNumber():
    biggest = 0
    x = 999
    y = 999

    while x > 0:
        y = 999
        while y > 0:
            number = x * y
            numStr = str(number)
            if stringIsPalindrome(numStr):
                if number > biggest:
                    biggest = number
            y-= 1
        x-=1
    
    return str(biggest)

value = biggestPalindromeNumber()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))