#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arg = []
    while True:
        n = len(arr)
        arg.append(n-arr.count(0))
        minimum = min(filter(lambda x: x > 0, arr))
        for i in range(0,n):
            if arr[i] > 0:
                if arr[i] - minimum < 0:
                    arr[i] = 0
                else:
                    arr[i] -= minimum
            else:
                continue
        if arr.count(0) == len(arr):
            return arg




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
