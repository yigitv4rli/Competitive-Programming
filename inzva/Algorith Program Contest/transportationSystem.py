n, m = list(map(int, input().strip().split()))

count = 0
result = list()

for i in range(n):
    inside = input()

    if i == n-1:
        newVersion = ""
        for char in inside[:m-1]:
            if char != "R":
                newVersion+= "R"
                count+=1
            else:
                newVersion+="R"
        newVersion+="F"
        result.append(newVersion)
    
    else:
        newVersion = ""
        
        if inside[-1] != "D":
            newVersion = inside[:m-1] + "D"
            count+=1
        else:
            newVersion = inside
        
        result.append(newVersion)

print(count)
for step in result:
    print(step)
        