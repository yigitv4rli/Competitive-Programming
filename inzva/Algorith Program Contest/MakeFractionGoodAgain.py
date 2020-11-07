p, q = list(map(int, input().strip().split()))
howMany2 = 0
howMany5 = 0
temp = q
division = True

while temp % 5 == 0:
    temp/=5
    howMany5+=1

while temp % 2 == 0:
    temp/=2
    howMany2+=1

if howMany2 % 3 != 0:
    amountTwo = (howMany2 // 3) +1
else:
    amountTwo = howMany2 // 3

amountFive = howMany5

if 40 % q == 0:
    print(1)
elif temp != 1:
    print(-1)
else:
    print(max(amountFive,amountTwo))