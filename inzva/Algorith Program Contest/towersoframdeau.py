N = int(input())
homes = list(map(int, input().strip().split()))

num = 1
maximum = homes[0]
for i in range(1,len(homes)):
    if homes[i] >= maximum:
        num+=1
        maximum = homes[i]

print(num) 
