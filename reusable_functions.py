def isPrime(number):
    if number > 1:
        i = 2
        while i < number: #bigger than 1 and smaller tha number
            if (number % i) == 0:
                return False
            i+= 1
        
        return True
    return False

def collatzSequence(number):
    sequence = []
    sequence.append(number)

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        sequence.append(number)
    
    return sequence



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