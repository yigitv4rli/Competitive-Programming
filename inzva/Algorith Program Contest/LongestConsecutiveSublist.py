N = int(input())
numbers = list(map(int, input().strip().split()))

numbers = sorted(list(set(numbers)))
lengthMax = 1

i = 1
while i < len(numbers):
    currentMax = 1
    for j in range(i,len(numbers)):
        if numbers[i-1] + 1 == numbers[i]:
            currentMax+=1
            i+=1
        else:
            lengthMax = max(lengthMax, currentMax)
            i = j+1
            break
    if i == len(numbers):
        lengthMax = max(lengthMax, currentMax)
        
    
print(lengthMax)


