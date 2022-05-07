from datetime import datetime

start = datetime.now()

def main():
    powToElab = pow(2,1000)
    charsOfPow = list(str(powToElab))
    numbers = [int(i) for i in charsOfPow]
    sumOf = sum(numbers)
    return sumOf


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))