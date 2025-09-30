#!/bin/python3

import os
import sys

def gradingStudents(grades):
    rounded = []
    for g in grades:
        if g < 38:
            rounded.append(g)  # failing grade, no rounding
        else:
            next_multiple = ((g // 5) + 1) * 5
            if next_multiple - g < 3:
                rounded.append(next_multiple)
            else:
                rounded.append(g)
    return rounded

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(sys.stdin.readline().strip())
    grades = [int(sys.stdin.readline().strip()) for _ in range(grades_count)]

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
