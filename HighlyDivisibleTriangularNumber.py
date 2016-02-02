from math import sqrt

def check(x):
    a = True
    
    for i in range(2,int(sqrt(x))+1):
        if (x % i) == 0:
            a = False
    return a

def main():
    
    lst = [1]
    
    prime = [2]
    
    k = 1
    while True:
           k += 1
           lst.append(lst[k-1]+k)
           
           while prime[-1]<lst[k]:
               count = 1
               while True:
                   if check(prime[-1]+1):
                       prime.append[prime[-1]+1]
                       break
                
               
               for i in prime:
                   if lst[k] % i == 0:
                       count += 1