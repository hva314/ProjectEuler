def check(x1):
    temp = ''
    for i in range(len(str(x1))-1,-1,-1):
        temp += str(x1)[i]
    x2 = int(temp)

    if x1-x2 == 0:
        return True
    else:
        return False

for i in range(999,0,-1):
    for j in range(i,1000):
        if check(i*j):
            print(i*j)
            break

        
