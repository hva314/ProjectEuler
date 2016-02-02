def main():
    
    global count
    global room

    with open('challenge5_in.txt') as f:
        N, line = [int(x) for x in f.readline().split()]
        board = ()

        for i in range(line):
            _1 , _2, _3, _4 = [int(x) for x in f.readline().split()]
            board += (((_1,_2),(_3,_4)),)
    
    room = [[0 for _ in range(N+2)] for _ in xrange(N+2)]    

    room[1][1] = 1
    
    def counton(room):
        on = 0

        for i in room:
            for j in i:
                if j>0:
                    on += 1

        return(on)

    def switch(room_x, room_y):
        global room
        
        for i in board:
            if i[0] == (room_x,room_y):
                room[i[1][0]][i[1][1]] = 1
    """
    def move(room_x,room_y,pre_x,pre_y):
        
        global square

        k = printon(room)

        if k ==line:
            return True

        print(room_x,room_y)
        
        if room[room_x][room_y] == 1:
            switch(room_x,room_y)
            room[room_x][room_y] = 2

        if room[room_x][room_y] == 2:
            if room[room_x+1][room_y]!=0 and room_x+1 != pre_x:
                move(room_x+1,room_y,room_x,room_y)

            if room[room_x][room_y+1]!=0 and room_y+1 != pre_y:
                move(room_x,room_y+1,room_x,room_y)

            if room[room_x-1][room_y]!=0 and room_x-1 != pre_x:
                move(room_x-1,room_y,room_x,room_y)

            if room[room_x-1][room_y]!=0 and room_y-1 != pre_y:
                move(room_x,room_y-1,room_x,room_y)
    """

    check = False
    global check
    
    def walkable(room_x,room_y):

        global check

        check = False

        pre_x = room_x
        pre_y = room_y

        def run(room_x,room_y,pre_x,pre_y):
        
            global check

            if (room_x,room_y)==(1,1):
                check = True
                return 0

            if room[room_x+1][room_y]!=0 and room_x+1 != pre_x:
                run(room_x+1,room_y,room_x,room_y)

            if room[room_x][room_y+1]!=0 and room_y+1 != pre_y:
                run(room_x,room_y+1,room_x,room_y)

            if room[room_x-1][room_y]!=0 and room_x-1 != pre_x:
                run(room_x-1,room_y,room_x,room_y)

            if room[room_x-1][room_y]!=0 and room_y-1 != pre_y:
                run(room_x,room_y-1,room_x,room_y)

        run(room_x,room_y,pre_x,pre_y)

        return check

    for i in range(line):
        for i in range(N+2):
            for j in range(N+2):
                
                if room[i][j] == 0:
                    pass
                elif room[i][j] == 1:
                    if walkable(i,j):
                        switch(i,j)
                        room[i][i] = 2
                
    for i in range(N+2):
        for j in range(N+2):
            if room[i][j] == 0:
                print('0'),
            else:
                print('1'),
        print('\n')
    print('Lighted rooms:'),
    print(counton(room))

if __name__ == '__main__':
    main()

