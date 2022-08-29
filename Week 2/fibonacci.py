
def fibo_slow(n) :
    if (n == 0) :
        return 0
    elif (n == 1) :
        return 1
    else :
        return (fibo_slow(n-1) + fibo_slow(n-2))

def main() :
    while(True) :
        n = int(input("Enter the value of n:\n"))
        print("The " + str(n) + "th fibonacci number is: " + str(fibo_slow(n)))

if __name__ == '__main__':   
    main()