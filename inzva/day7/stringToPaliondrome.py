import collections

def isPalindrome(string):
    if string == string[::-1]:
        return 1 
    else:
        return 0

s = input()
length = len(s)

k = length - collections.Counter(s).most_common(1)[0][1]
if length % 2 == 0:
    p1 = int(length / 2) - 1
    p2 = int(length /2)
else:
    p1 = int(length / 2) - 1
    p2 = int(length /2) + 1


totalCost = 0
while p1 >= 0:
    first = s[p1]
    second = s[p2]

    if first != second:
        cost1 = s.count(first)
        cost2 = s.count(second)

        if cost1 > cost2:
            s = s.replace(second, first)
            totalCost+=cost2
        else:
            s = s.replace(first, second)
            totalCost+=cost1

    p1-=1
    p2+=1

    if isPalindrome(s):
        break

print(min(totalCost, k))
