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

    return result

def isPrime(number):
    if number > 1:
    # check for factors
        i = 2
        while i < number:
            if (number % i) == 0:
                return False
            i+= 1
        
        return True

value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))