
# Bubble Sort

import random


def bubbleSortFast(A) :
    chk = False
    n = len(A)
    for a in range(2) :
        for b in range(n-1-a) :
            if (A[b] > A[b+1]) :
                chk = True
                tmp = A[b]
                A[b] = A[b+1]
                A[b+1] = tmp
        if (chk == False) :
            break
    return (A[n-2] * A[n-1])

def bubbleSort(A) :
    n = len(A)
    max_index1 = -1
    for i in range(n) :
        if((max_index1 == -1) or (A[i] > A[max_index1])) :
            max_index1 = i

    max_index2 = -1
    for j in range(n) :
        if((j != max_index1) and ((max_index2 == -1) or (A[j] > A[max_index2]))) :
            max_index2 = j

    return (A[max_index1]*A[max_index2])

def main() :
    while(True) :
        n = random.randint(2,1000)
        print(n)
        A = []
        for i in range(n) :
            A.append(random.randint(0,100000))
            print(A[i], end = " ")
        print()
        res1 = bubbleSort(A)
        res2 = bubbleSortFast(A)
        if (res1 != res2) :
            print("Wrong answer: " + str(res1) + " " + str(res2))
            break
        else :
            print("OK")

if __name__ == '__main__':   
    main()