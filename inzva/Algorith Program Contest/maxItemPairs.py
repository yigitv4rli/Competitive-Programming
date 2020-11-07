amounts = list(map(int, input().strip().split()))
amounts.sort()
count = 0

while amounts[0] or amounts[1]:
    amounts[1]-=1
    amounts[2]-=1
    count+=1
    amounts.sort()

print(count)