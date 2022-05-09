from datetime import datetime

start = datetime.now()

def smallestDivisibleNumber1to20():

    dividers = range(1,20)
    number = 20
    while True:
        divisible = True
        for divider in dividers:
            if number % divider != 0:
                divisible = False
        if divisible:
            return number
        number += 1

value = smallestDivisibleNumber1to20()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))