N = int(input())
x, y = list(map(int, input().strip().split()))
prev_x, prev_y = x, y

corners = list()
corners.append([x,y])
for i in range(N-1):
    x, y = list(map(int, input().strip().split()))

    if x == prev_x and y <= prev_y:
        continue
    elif y > prev_y:
        j = 0
        for i in range(0,len(corners)):
            if corners[j][1] <= y:
                corners.remove(corners[j])
            else:
                j+=1
        
        corners.append([x,y])
        prev_x = x
        prev_y = y
    else:
        corners.append([x,y])
        prev_x = x
        prev_y = y
        

amountCorner = len(corners)
area = corners[0][0]* corners[0][1]

for i in range(1,amountCorner):
    area+= ((corners[i][0] - corners[i-1][0]) * corners[i][1])

print(area*4)

