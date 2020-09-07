S = input()
T = input()

length = len(S)
index = 0

while index < length:
    letter1 = S[index]
    letter2 = T[index]

    if letter1 != letter2:
        if S.find(letter1) < index:
            break
        S = S.replace(letter1, '#')
        S = S.replace(letter2,letter1)
        S = S.replace('#',letter2)
    index+=1

if S != T:
    print("NO")
else:
    print("YES")
