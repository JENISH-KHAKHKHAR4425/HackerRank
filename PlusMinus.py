import math
import os
import random
import re
import sys

def plusMinus(arr):
    total = len(arr)
    if total == 0:
        print("0.000000")
        print("0.000000")
        print("0.000000")
        return
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    print("{:.6f}".format(positive / total))
    print("{:.6f}".format(negative / total))
    print("{:.6f}".format(zero / total))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
