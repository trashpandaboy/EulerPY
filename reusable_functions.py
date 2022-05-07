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
    
def sumOfDigits(number):
    charsOfNumber = list(str(number))
    numbers = [int(i) for i in charsOfNumber]
    return sum(numbers)

def stringIsPalindrome(value):
    if value == value[::-1]:
        return True
    else:
        return False