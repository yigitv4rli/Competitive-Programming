values1 = list(map(int, input().strip().split()))
values = list(map(int, input().strip().split()))

stockPrice = values1[0]
K = values1[1]

increases = [-1]
decreases = [-1]

incStart, incEnd = 0, 0
currIndex = 0

while currIndex < stockPrice-1:
    incStopped = True
    temp = 10**7
    secMinIndex = currIndex+1
    while currIndex < stockPrice - 1 and values[incStart] <= values[currIndex+1]:
        if incEnd-incStart <= K-1:
            if temp >= values[currIndex+1]:
                temp = values[currIndex+1]
                secMinIndex = currIndex+1

            incEnd+=1
            currIndex+=1

            incPerc = ((values[incEnd] - values[incStart]) / values[incStart]) * 100
            increases.append(incPerc)
        else:
            incStopped = False
            break


    if incStopped == False:
        currIndex = secMinIndex
        incEnd = currIndex
        incStart = currIndex
    else:        
        incEnd+=1
        incStart = incEnd
        currIndex = incStart


decStart, decEnd = 0, 0
currIndex = 0

while currIndex < stockPrice-1:
    decStopped = True
    temp = 0
    secMaxIndex = currIndex+1
    while currIndex < stockPrice -1 and values[decStart] >= values[currIndex+1]:
        if decEnd-decStart <= K-1:
            if temp <= values[currIndex+1]:
                temp = values[currIndex+1]
                secMaxIndex = currIndex+1

            decEnd+=1
            currIndex+=1

            decPerc = ((values[decStart] - values[decEnd])/ values[decStart]) * 100
            decreases.append(decPerc)
        else:
            decStopped = False
            break

    if decStopped == False:
        currIndex = secMaxIndex
        decEnd = currIndex
        decStart = currIndex
    else:
        decEnd+=1
        decStart = decEnd
        currIndex = decStart


print("{:.6f}".format(max(decreases)))
print("{:.6f}".format(max(increases)))
