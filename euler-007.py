from reusable_functions import isPrime
from datetime import datetime

start = datetime.now()

def main():
    primesFounds = 0
    number = 0
    max = 10001
    while primesFounds < max:
        number +=1
        if isPrime(number):
            primesFounds += 1
        
    return number

value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))