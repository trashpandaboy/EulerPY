from datetime import datetime
from reusable_functions import factorial
from reusable_functions import sumOfDigits

start = datetime.now()

def main():
    result = factorial(100)
    return sumOfDigits(result)


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))