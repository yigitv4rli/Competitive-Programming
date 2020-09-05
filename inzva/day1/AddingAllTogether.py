numbers = int(input())
values = list(map(int , input().split()))
p2 = 1
total = 0
for index in range(numbers) : 
    total+= p2* values[index] * numbers
    p2+=1
    numbers-=1

print(total)
