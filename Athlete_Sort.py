#!/bin/python3

import math
import os
import random
import re
import sys

def bubble_sort(arg,k):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(arg)-1):
            if arg[i][k] > arg[i+1][k]:
                arg[i], arg[i+1] = arg[i+1], arg[i]
                swapped = True
    return arg

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    last = (bubble_sort(arr,k))
    for lists in last:
        lists = map(str,lists)
        print(" ".join(lists))


