

def fibonacci(goal, prev1, prev2, list):
    new = prev1 + prev2
    if  new <= goal:
        prev1 = prev2
        prev2 = new
        if new % 2 == 0:
            list.append(new)
        fibonacci(goal, prev1, prev2, list)
    else:
        return list

numbers = []
fibonacci(4000000, 0, 1, numbers)

print(numbers)

print("The sum is " + str(sum(numbers)))

