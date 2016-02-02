def main():
    
    k = 1
    loc = 1

    for a in range(1000000):
        n = a
        print('\n')
        
        count = 1

        while a>1:
            
            print(a),
            print('->'),
            
            if a%2==0:
                a = a//2
                count += 1

            elif a%2==1:
                
                a = a*3+1
                count += 1

        if count>k:
            k = count
            loc = n

    print
    print(k,loc)

main()
