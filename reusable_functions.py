def isPrime(number):
    if number > 1:
        i = 2
        while i < number: #bigger than 1 and smaller tha number
            if (number % i) == 0:
                return False
            i+= 1
        
        return True
    return False

def factorial(number):
    if(number > 1):
        return number * factorial(number-1)
    else:
        return number