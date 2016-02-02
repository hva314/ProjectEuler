def check(i,j,k):
    if i*i+j*j==k*k:
        return True
    elif i*i+k*k==j*j:
        return True
    elif k*k+j*j==i*i:
        return True
    else:
        return False

def main():
    
    n = int(input('Type in the number: '))
    
    for i in range(3,n-2):
        for j in range(i+1,n-i):
            if check(i,j,1000-i-j):
                print(i,j,1000-i-j)
                
                    
main()