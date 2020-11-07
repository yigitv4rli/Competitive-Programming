N = int(input())
string = input()

first = 0
second = 0

for i in range(0,N):
    if i % 2 == 0 and string[i] != "1":
        first+=1
    elif i % 2 == 1 and string[i] != "0":
        first+=1

for i in range(0,N):
    if i % 2 == 0 and string[i] != "0":
        second+=1
    elif i % 2 == 1 and string[i] != "1":
        second+=1

        


print(min(first,second))