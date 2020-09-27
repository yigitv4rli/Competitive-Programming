X = int(input())
Y = int(input())

number = list()

while True:
    X = X % Y
    old = X
    X = pow(X,X,Y)
    
    if X == 1:
        print(1)
        break

    if old == X:
        print(X)
        break
    elif X in number:
        print("IMPOSSIBLE")
        break
    else:
        number.append(X)
