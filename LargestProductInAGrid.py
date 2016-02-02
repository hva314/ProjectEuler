def main():
    
    f = open('LargestProductInAGrid.txt','r')
    
    lstNum = []
    
    for i in f.readlines():
        temp = []
        for j in i.split():
            temp.append(int(j))
        lstNum.append(temp)
        
        
    width = len(lstNum[0])
    
    height = len(lstNum)
    
    intMax = 1    
    
    for i in range(width-3):
        for j in range(height-3):
            
            intProduct = lstNum[i][j]*lstNum[i+1][j+1]*lstNum[i+2][j+2]*lstNum[i+3][j+3]
            if intProduct > intMax:
                intMax = intProduct
                
    for i in range(3,width):
        for j in range(height-3):
            
            intProduct = lstNum[i][j]*lstNum[i-1][j+1]*lstNum[i-2][j+2]*lstNum[i-3][j+3]
            if intProduct > intMax:
                intMax = intProduct

    for i in range(width-3):
        for j in range(height):

            intProduct = lstNum[i][j]*lstNum[i+1][j]*lstNum[i+2][j]*lstNum[i+3][j]
            if intProduct > intMax:
                intMax = intProduct

    for i in range(width):
        for j in range(height-3):

            intProduct = lstNum[i][j]*lstNum[i][j+1]*lstNum[i][j+2]*lstNum[i][j+3]
            if intProduct > intMax:
                intMax = intProduct
                
    print(intMax)
        
main()       