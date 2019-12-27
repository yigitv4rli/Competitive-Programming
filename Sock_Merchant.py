#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    stack = []
    pair_count = 0
    for i in range(0,n):
        if ar[i] not in stack:
            stack.append(ar[i])
        else:
            stack.pop(stack.index(ar[i]))
            pair_count +=1
    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
