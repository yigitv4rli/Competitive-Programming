values = list(map(int, input().strip().split()))
N, k = values[0], values[1]
array = list(map(int, input().strip().split()))


for i in range(N):
    if array[i] == 1:
        first = i
        break

count, total = 0, 0
for i in range(N):
    if array[i] == 1 :
        count+=1
    else:
        continue

    if count == k:
        p1, p2 = 0, 0
        total+=1
        
        for j in range(i+1, N):
            if array[j] == 0:
                total+=1
                p1+=1
            else:
                break
        
        for j in range(first-1,-1,-1):
            if array[j] == 0:
                total+=1
                p2+=1
            else:
                break
        
        for j in range(first+1,N):
            if array[j] == 1:
                first = j
                break
        total+= p1*p2
        count-=1
        
print(total)
