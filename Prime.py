from math import sqrt

def check(x):
    a = True
    
    for i in range(2,int(sqrt(x))+1):
        if (x % i) == 0:
            a = False
    return a

def main():

    k = 0
    i = 2

    while k <= 20000000:
        if check(i):
            print(i)
            k += 1
            print('--->',k)
        i += 1

main()
