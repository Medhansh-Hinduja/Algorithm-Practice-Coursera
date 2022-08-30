
def gcd_slow(a,b) :
    for i in reversed(range(1,min(a,b)+1)) :
        if ((a % i == 0) and (b % i == 0)) :
            return i

# uses the Euclidean Algorithm
def gcd_better(a,b) :
    if (a == 0) :
        return b
    elif (b == 0) :
        return a
    elif (a == b) :
        return a
    elif (a > b) :
        a = a%b
        return gcd_better(a,b)
    else :
        b = b%a
        return gcd_better(a,b)

def main() :
    while(True) :
        a = int(input("Enter the first number:\n"))
        b = int(input("Enter the second number:\n"))
        slow = gcd_slow(a,b)
        better = gcd_better(a,b)
        print("The slow gcd is: " + str(slow))
        print("The better gcd is: " + str(better))

if __name__ == '__main__':   
    main()