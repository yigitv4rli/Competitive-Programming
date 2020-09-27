from functools import reduce

T = int(input())
nazif = list()
osman = list()

for i in range(T):
    values = list(map(int, input().strip().split()))
    nazif.append(values[0])
    osman.append(values[1])

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for i in range(T):
    a = len(factors(nazif[i]))
    b = len(factors(osman[i]))

    if a > b:
        print("nazif")
    elif b > a:
        print("osman")
    else:
        print("tie")
