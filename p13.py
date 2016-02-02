def main():
    f = open('p13.in','r')
    sum = 0
    for i in f.readlines():
        sum += int(i)
    print(sum)

main()
