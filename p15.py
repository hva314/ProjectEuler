# room = [[0 for _ in range(20)] for _ in xrange(20)]

global count 
count = 0

def run(x,y):

    global count

    if x == 21 and y == 21:
        count += 1
        return 0

    if x+1<22:
        run(x+1,y)

    if y+1<22:
        run(x,y+1)

run(1,1)
print("=====> ",count)

    
