from math import comb

pencils = int(input())

combNumber = 0

for i in range(1,pencils+1, 2):
    combNumber += comb(pencils, i)

print(combNumber)