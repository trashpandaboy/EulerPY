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

def listOfFirst10KPrimes():
    first10KPrimes = []

    primesFounds = 0
    number = 0
    max = 10000
    while primesFounds <= max:
        number +=1
        if isPrime(number):
            primesFounds += 1
            first10KPrimes.append(number)
    
    return first10KPrimes
        

def getMonthDays(month, year):
    if month == 4 or month == 6 or month ==  9 or month == 11:
        return 30
    elif month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    else:
        return 31

def isYearLeap(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def getAmountOfDivisors(number):
    amount = 0

    i = 1
    while i * i < number:
        if number % i == 0:
            amount+=1
        i+=1

    if i - (number / i) == 1:
        i-=1

    while i >= 1:
        if number % i == 0:
            amount+=1
        i-=1
        
    return amount

def getProperDivisors(number):
    divisors = []

    i = 1
    while i * i < number:
        if number % i == 0:
            divisors.append(i)
        i+=1

    if i - (number / i) == 1:
        i-=1

    while i > 1:
        if number % i == 0:
            divisors.append(number / i)
        i-=1
    
    return divisors


def getTriangleNumberOfNumber(number):
    triangleNumber = 0
    while number > 0:
        triangleNumber += number
        number -= 1
    
    return triangleNumber

def getStringValue(string):
    valueOfString = 0
    
    string = string.upper()

    for letter in string:
        value = ord(letter)
        valueOfString += (value - 64)
        
    return valueOfString