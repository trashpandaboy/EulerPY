from datetime import datetime

start = datetime.now()

def main():
    # k = 1
    # n = 1
    # m = 0
    # found = False

    # iterations = 0
    # canGo = True
    # while k < 100:
    #     while n < 1000:
    #         m = n+1
    #         while m < 1000:

    #             A = m*m - n*n
    #             B = 2*(m*n)
    #             C = m*m + n*n
    #             sumABC = A+B+C

    #             if(A<B and B<C):
    #                 print("A: %s - B: %s - C: %s - Sum: %s"%(str(A), str(B), str(C), str(sumABC)))
                    
    #                 if(sumABC == 1000):
    #                     print("found")
    #                     found = True
    #                     input()
    #                     break
                
    #             m+=1
    #         n+=1
    #     k+=1

    sum = 1000
    a = 1
    while a <= sum / 3:
        b = a + 1
        while b <= sum/2:
            c = sum - a - b
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