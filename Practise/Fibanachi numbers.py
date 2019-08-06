

qty = input("How many Fibonacci numbers would you like to generate?\n")
fibonacciSequence = []

def createFibonacci(qty):
    global fibonacciSequence
    count = 0
    print("\nFibonacci sequence:")
    while count < int(qty):
        if (len(fibonacciSequence)==0):
            fibonacciSequence.append(0)
            count += 1
        if (len(fibonacciSequence)==1):
            fibonacciSequence.append(1)
            count += 1
        if len(fibonacciSequence) >= 2:
            nextVal = (fibonacciSequence[len(fibonacciSequence)-1] + fibonacciSequence[len(fibonacciSequence)-2])
            fibonacciSequence.append(nextVal)
        count += 1

def displayFibonacciSequence():
    global fibonacciSequence
    for x in fibonacciSequence:
        print(x)

createFibonacci(qty)
displayFibonacciSequence()