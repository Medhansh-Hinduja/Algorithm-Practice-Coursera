
def fibo_slow(n) :
    if (n == 0) :
        return 0
    elif (n == 1) :
        return 1
    else :
        return (fibo_slow(n-1) + fibo_slow(n-2))

def fibo_better(n) :
    A = []
    A.append(0)
    A.append(1)
    for i in range(2, n+1) :
        A.append(A[i-1] + A[i-2])
    return A[n]

def main() :
    while(True) :
        n = int(input("Enter the value of n:\n"))
        print("Slow approach")
        print("The " + str(n) + "th fibonacci number is: " + str(fibo_slow(n)))
        print("Better approach")
        print("The " + str(n) + "th fibonacci number is: " + str(fibo_better(n)))

if __name__ == '__main__':
    main()