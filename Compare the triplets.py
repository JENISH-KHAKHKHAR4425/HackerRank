import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    return [alice_score, bob_score]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()



#Constraints:
1 ≤ a[i] ≤ 100
1 ≤ b[i] ≤ 100
#Sample Input 0:
5 6 7
3 6 10
#Sample Output 0:
1 1
