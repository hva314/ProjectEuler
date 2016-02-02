from math import sqrt

def check(x):
    a = True
    
    for i in range(2,int(sqrt(x))+1):
        if (x % i) == 0:
            a = False
    return a

def main():

    sum = 0
    i = 2

    while i < 2000000:
        if check(i):
            print(i)
            sum += i
        i += 1
    
    print(sum)

main()
