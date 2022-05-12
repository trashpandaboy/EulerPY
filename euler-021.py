from datetime import datetime

from reusable_functions import getProperDivisors

start = datetime.now()

def main():
    number = 1
    amicableNumbers = []

    while number < 10000:
        #calculate the sum of proper divisors of number
        divisorsSum = sum(getProperDivisors(number))
        #calculate the sum of proper divisors of divisorsSum
        divisorsSumOfSum = sum(getProperDivisors(divisorsSum))
        
        if number == divisorsSumOfSum:
            if(number != divisorsSum): #if they're not equals then are amicable
                print("d(%s) = %s - d(%s) = %s"%(str(number),str(divisorsSum),str(divisorsSum),str(divisorsSumOfSum),))
                #add them in the list only if not already in
                if number not in amicableNumbers:
                    amicableNumbers.append(number)
                if divisorsSum not in amicableNumbers:
                    amicableNumbers.append(divisorsSum)

        number+=1

    print(amicableNumbers)
    return sum(amicableNumbers) #sum them to obtain the total value


value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))