#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    page_numbers_front = [0,1]
    page_numbers_back = [n,n+1] if n%2 == 0 else [n-1,n]
    count_front = 0
    count_back = 0
    if p % 2 == 0:
        while page_numbers_front[0] != p and page_numbers_back[0] != p:
            page_numbers_front[0] += 2
            count_front +=1
            page_numbers_back[0] -=2
            count_back +=1
        return min(count_back,count_front)
    else:
        while page_numbers_front[1] != p and page_numbers_back[1] != p:
            page_numbers_front[1] += 2
            count_front +=1
            page_numbers_back[1] -=2
            count_back +=1
        return min(count_back,count_front)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
