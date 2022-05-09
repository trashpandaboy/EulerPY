
from cgitb import small
from datetime import datetime

start = datetime.now()

def main():
    target = 2000000
    sum = 0
    number = 0
    while number < target:
        if(number % 10000 == 0):
            print(number)
            
        if isPrime(number):
            sum += number
        number +=1
        
    return sum

def isPrime(number):
    if number > 1:
    # check for factors
        i = 2
        while i < number: #bigger than 1 and smaller tha number
            if (number % i) == 0:
                return False
            i+= 1
        
        return True

value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))