import sys

def display(area, side):

    print(side)

    side_xy = 6-(side+1)/2

    for i in range(side_xy,side_xy+side):
        for j in range(side_xy,side_xy+side):
            
            num = area[j][i]

            if num==100:
                print(num),
                            
            elif num>9:
                print(str(num)+' '),

            else:
                print(str(num)+'  '),
        print
    print


def main():
    
    side = 13

    square = [[0 for i in range(side)] for i in xrange(side)]

    end_x = 5
    end_y = 5
    square[end_x][end_y] = 1

    for d in range(2,side):

        temp_list = [i for i in range(d**2-d*2+2,d**2+1)]
        temp_list1 = temp_list[:len(temp_list)/2+1]
        temp_list2 = temp_list[len(temp_list)/2+1:]

        if d%2==0 :

            start_x = end_x + 1
            start_y = end_y 

            for i in temp_list1:

                square[start_x][start_y] = i
                start_y += 1

            start_x -= 1
            start_y -= 1

            for i in temp_list2:

                square[start_x][start_y] = i
                start_x -= 1

            start_x += 1

            end_x = start_x
            end_y = start_y

        if d%2==1 :

            start_x = end_x - 1
            start_y = end_y

            for i in temp_list1:

                square[start_x][start_y] = i
                start_y -= 1

            start_x += 1
            start_y += 1

            for i in temp_list2:

                square[start_x][start_y] = i
                start_x += 1
            
            start_x -= 1

            end_x = start_x
            end_y = start_y
        
        display(square,d)

if __name__ == '__main__':
    if sys.version_info > (3,0):
        print('Please use python2 only!')
    else:
        main()

