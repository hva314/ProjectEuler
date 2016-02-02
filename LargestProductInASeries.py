def main():
    f = open('LargestProductInASeries.txt','r')
    
    lstChar = []
    
    while True:
        i = f.read(1)
        if not i:
            break
        lstChar.append(i)
        
    intMax = 0    
    
    for i in range(len(lstChar)-13):
        intProduct = 1
        for j in range(13):
            intProduct *= int(lstChar[i+j])
        
        if intProduct>intMax:
            intMax = intProduct
    
    print(intMax)    
    
main()