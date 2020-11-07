values = list(map(int, input().strip().split()))
N = values[0]
W = values[1]

prices = list(map(int, input().strip().split()))
maximum = 0

newL = list()
for price in prices:
    if price < W:
        newL.append(price)
    if W % price == 0:
        print(W)
        exit()

newL = list(set(newL))
newL = sorted(newL)
length = len(newL)

indexDict = {}
for indices, item in enumerate(newL):
    indexDict[item] = indices

if length == 0:
    print(0)
elif length == 1:
    print((W//newL[0]) * newL[0])
else:
    maximum, currTotal = 0, 0
    index, secIndex = 0, 0
    stack = []
    while index < length:
        element = newL[secIndex]
        if currTotal + element <= W:
            currTotal+= element
            stack.append(element)
            maximum = max(maximum, currTotal)

            if W % currTotal == 0:
                maximum = W
                break
            
        else:
            if len(stack) == 0:
                break
            poppedElement = stack.pop()
            currTotal-= poppedElement
            secIndex = indexDict[poppedElement]+1

            if len(stack) == 0:
                index+=1
                secIndex = index
                stack = list()
                total = 0
            elif length == secIndex:
                poppedElement = stack.pop()
                currTotal-= poppedElement
                secIndex = indexDict[poppedElement]+1
            
    print(maximum)

