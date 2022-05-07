
from cgitb import small
from datetime import datetime

start = datetime.now()

def main():
    squares = []
    max = 100
    sumOfNumbers = sum(range(1,max+1))
    i = 1
    while i <= max:
        squares.append(i*i)
        i+=1

    sumOfSquare = sum(squares)
    
    squareOfSum = sumOfNumbers * sumOfNumbers
    
    result = squareOfSum - sumOfSquare

    return result


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))