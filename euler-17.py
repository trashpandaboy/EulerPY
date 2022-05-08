from datetime import datetime

from reusable_functions import sumOfDigits

start = datetime.now()

def main():
    numbers = list(range(1,1000))

    totalLenght = 0
    for number in numbers:
        stringOfNumber = numberToString(number)
        lenghtOfNumber =    len(stringOfNumber.strip())
        totalLenght += lenghtOfNumber
        # print(str(number) + ": " + stringOfNumber)
        # print("Lenght: " + str(lenghtOfNumber))
        # print("New TotalLenght: " + str(totalLenght))

    return totalLenght + len("onethousand")


def numberToString(number):
    baseString = str(number)
    numberLenght = len(baseString)

    if(numberLenght > 1):
        if(numberLenght == 2):
            stringNumber = ""
            if(baseString.startswith('1')):
                stringNumber = "ten"
            elif(baseString.startswith('2')):
                stringNumber = "twenty"
            elif(baseString.startswith('3')):
                stringNumber = "thirty"
            elif(baseString.startswith('4')):
                stringNumber = "forty"
            elif(baseString.startswith('5')):
                stringNumber = "fifty"
            elif(baseString.startswith('6')):
                stringNumber = "sicty"
            elif(baseString.startswith('7')):
                stringNumber = "seventy"
            elif(baseString.startswith('8')):
                stringNumber = "eighty"
            elif(baseString.startswith('9')):
                stringNumber = "ninety"
            if(number % 10 == 0):
                return stringNumber
            elif not baseString.startswith('1'):
                return stringNumber + "" + numberToString(int(baseString[1:]))
            elif baseString.startswith('1'):
                if baseString.endswith('1'):
                    return "eleven"
                elif baseString.endswith('2'):
                    return "twelve"
                elif baseString.endswith('3'):
                    return "thirteen"
                elif baseString.endswith('4'):
                    return "fourteen"
                elif baseString.endswith('5'):
                    return "fifteen"
                elif baseString.endswith('6'):
                    return "sixteen"
                elif baseString.endswith('7'):
                    return "seventeen"
                elif baseString.endswith('8'):
                    return "eighteen"
                elif baseString.endswith('9'):
                    return "nineteen"
        if(numberLenght == 3):
            stringNumber = numberToString(int(baseString[0:1])) + "hundred"
            secondHalf = numberToString(int(baseString[1:3]))
            if secondHalf.strip() != "":
                stringNumber += "and" + secondHalf

            return stringNumber
                
    else:
        if(number == 1):
            return "one"
        elif(number == 2):
            return "two"
        elif(number == 3):
            return "three"
        elif(number == 4):
            return "four"
        elif(number == 5):
            return "five"
        elif(number == 6):
            return "six"
        elif(number == 7):
            return "seven"
        elif(number == 8):
            return "eight"
        elif(number == 9):
            return "nine"
    
    return ""


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))