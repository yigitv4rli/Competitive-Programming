N = int(input())
nums = list(map(int, input().strip().split()))

firstMax = max(nums)

if nums.count(firstMax) > 1:
    for num in nums:
        print(firstMax, end=" ")
else:
    secondmax = 0
    for num in nums:
        if num == firstMax:
            continue
        elif num > secondmax:
            secondmax = num
    
    for num in nums:
        if num == firstMax:
            print(secondmax, end=" ")
        else:
            print(firstMax, end=" ")