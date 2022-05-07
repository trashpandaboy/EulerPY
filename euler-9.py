from datetime import datetime

start = datetime.now()

def main():
    sumOfTriplet = 1000
    a = 1
    while a <= sumOfTriplet / 3:
        b = a + 1
        while b <= sumOfTriplet / 2:
            c = sumOfTriplet - a - b
            if a*a + b*b == c*c:
                product = a*b*c
                print(str(product))
            b+=1
        a+= 1

    return 0

value = main()
print(value)

end = datetime.now()
print("The time of execution of above program is :",
      str(end-start))