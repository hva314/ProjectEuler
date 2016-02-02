import math

def main():
    
    # list of prime number
    global prime

    sum_number = [1]
    prime = [2]

    # normal checking prime number function
    # return True/False
    def check_prime(n):
        if n % 2 == 0 and n > 2: 
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    # find a bigger prime number than a
    # return that prime number
    def add_prime(a):
        
        a += 1
        while True:
            if check_prime(a):
                return a
            else:
                a += 1

    # getting number of divisor
    def get_div(num):
        
        global prime

        # check if the list of prime number is 
        # long enough to contain 'all' the possible divisor
        while prime[-1]<(num/2+1):
            prime.append(add_prime(prime[-1]))

        # starting total divisor is 1
        total_div = 1

        num_run = num

        # divide all the number in the prime list by the num_run
        for i in prime:
            count = 0
            while num_run != 1:
                if num_run%i == 0:
                    num_run = num_run/i
                    count += 1
                else:
                    break
            count += 1

            # calculating the total div according to
            # x = a^n+b^m+... (a,b,... is prime)
            # then divisor of x is (n+1)(m+1)...
            total_div = total_div * count

        return total_div

    # sum_number is list contain all the triangle number
    count = 1
    div = 1

    while div < 500:

        div = get_div(sum_number[-1])
        count += 1
        sum_number.append(sum_number[-1]+count)

    print(sum_number[-2])


# for the purpose of the program, all the prime number should get the number of divisor of 1
# due to the process of limitting the prime number checking

main()
