stockPrice = int(input())
values = list(map(int, input().strip().split()))

increases = [-1]
decreases = [-1]

incStart, incEnd = 0, 0
currIndex = 0

"13674 85406 7509 50541 8040 69104 56573 58070"
while currIndex < stockPrice-1:
    while currIndex < stockPrice - 1 and values[incStart] < values[currIndex+1]:
        incEnd+=1
        currIndex+=1

        incPerc = ((values[incEnd] - values[incStart]) / values[incStart]) * 100
        increases.append(incPerc)
    
    incEnd+=1
    incStart = incEnd
    currIndex = incStart


decStart, decEnd = 0, 0
currIndex = 0

while currIndex < stockPrice-1:
    while currIndex < stockPrice -1 and values[decStart] > values[currIndex+1]:
        decEnd+=1
        currIndex+=1
        
        decPerc = ((values[decStart] - values[decEnd])/ values[decStart]) * 100
        decreases.append(decPerc)

    decEnd+=1
    decStart = decEnd
    currIndex = decStart

print(max(decreases), max(increases), sep="\n")
