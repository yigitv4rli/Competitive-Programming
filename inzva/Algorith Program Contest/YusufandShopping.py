N, k = list(map(int, input().strip().split()))

result = [0] * (10**5)
for i in range(N):
    amount, unitPrice = list(map(int, input().strip().split()))
    result[unitPrice-1] += amount 

m = 0
for i in range(10**5):
    m+=result[i]

    if m >= k:
        print(i+1)
        break