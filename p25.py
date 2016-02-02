fibo = [1,1]
index = 2

while True:

    fibo.append(fibo[index-2]+fibo[index-1])
    index += 1
    
    if len(str(fibo[-1]))>=1000:
        print(index)
        print(fibo[-1])
        break
