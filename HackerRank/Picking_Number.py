#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    length = len(a)
    n = 0
    a = sorted(a)
    max_pairs = 0
    for i in range(0,length):
        counter = 0
        for j in range(i,length):
            if a[j] - a[i] == 0 or a[j] - a[i] == 1:
                counter +=1
        max_pairs = max(max_pairs,counter)
    return max_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
