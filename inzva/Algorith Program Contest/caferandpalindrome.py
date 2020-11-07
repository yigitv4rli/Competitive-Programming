N = int(input())
string = input()

chars = dict()

for char in string:
    if char not in chars.keys():
        chars[char] = 1
    else:
        chars[char]+=1

odd = 0
for key in chars.keys():
    if chars[key] % 2 == 1:
        odd+=1
    if odd > 1:
        break

if(odd>1):
    print("NO")
else:
    print("YES")