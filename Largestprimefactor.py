from math import  *

def check(x):
    a = True
    
    for i in range(2,int(sqrt(x))+1):
        if (x % i) == 0:
            a = False
            break
    return a


def main():
    
    lstPrime = []
    
    intNum = int(input('Type your number: '))
    
    k = 2
    while intNum > 1:
        if intNum % k != 0:
            k += 1
        else:
            if check(k):
                print(k)
                intNum = intNum/k

main()