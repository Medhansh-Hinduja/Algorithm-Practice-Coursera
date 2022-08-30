import random

# This is a stress testing script to check whether my implementation of the Euclidean Algorithm is correct, using another correct implementation

# My implementation
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

# Implementation using Euclid's Lemma
def gcd_correct(a,b) :
    if (b == 0) :
        return a
    c = a%b
    return gcd_correct(b, c)

def main() :
    while(True) :
        a = random.randrange(1,100000000000)
        print(a)
        b = random.randrange(1,100000000000)
        print(b)
        res1 = gcd_better(a,b)
        res2 = gcd_correct(a,b)
        if (res1 != res2) :
            print("Wrong answer: " + str(res1) + " " + str(res2))
            break
        else :
            print("OK")

if __name__ == '__main__':   
    main()

# WORKS PERFECTLY