com = list(map(int, input().strip().split()))
types, dollars = com[0], com[1]

candyNumbers = []
candyCosts = []
for i in range(types):
    candy = list(map(int, input().strip().split()))
    candyNumbers.append(candy[0])
    candyCosts.append(candy[1])

totalBought = 0
buy = True
while buy:
    minCost = min(candyCosts)
    minIndex = candyCosts.index(minCost)

    canBought = min(candyNumbers[minIndex], dollars//candyCosts[minIndex])

    if canBought == 0:
        buy = False
    else:
        totalBought += canBought
        dollars-= candyCosts[minIndex] * canBought

    del candyNumbers[minIndex]
    del candyCosts[minIndex]

print(totalBought)
