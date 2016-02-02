def check(x):
    for i in range(20):
        if x%(i+1) != 0:
            return False
            break
    return True

def main():

    i =1
    c = True
    while c:
        print(i)
        if check(i):
            print(i)
            c = False
        i += 1

main()
        
