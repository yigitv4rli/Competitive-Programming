n = int(input())
s = input()
t = input()

total = 0
i = 0
passCount = 1
while i < n:
    if s[i] < t[i]:
        total += (n - i) * passCount
        passCount = 1
    elif s[i] == t[i]:
        passCount+=1
    else:
        passCount = 1
    i += 1       

print(total)
