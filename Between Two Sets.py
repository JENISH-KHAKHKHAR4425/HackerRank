import math
import os
import sys


def getTotalX(a, b):
    # Function to compute LCM of two numbers
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    # Function to compute LCM of a list
    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = lcm(lcm_a, num)

    # Function to compute GCD of a list
    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = math.gcd(gcd_b, num)

    # Count multiples of lcm_a that divide gcd_b
    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
