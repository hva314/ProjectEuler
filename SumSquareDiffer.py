def sumsquare(x):
    
    return int((x*(x+1)*(2*x+1))/6)

def squaresum(x):

    return int(((x+1)*x)/2)

def main():

    x = int(input('Type in the number: '))

    print(sumsquare(x))
    print(squaresum(x))

    print(abs(sumsquare(x)-squaresum(x)))

main()
