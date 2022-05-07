from datetime import datetime

from reusable_functions import sumOfDigits

start = datetime.now()

def main():
    powToElab = pow(2,1000)
    return sumOfDigits(powToElab)


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))