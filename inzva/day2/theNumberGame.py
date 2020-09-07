turn = int(input())
kekik = list()
haydarberk = list()

kekikP, haydarberkP = 0, 0

def pointCalc(number):
    round = 0
    while number != 1:
        if number % 2 == 1:
            number = number * 3 +1
            round+=1
        elif number % 2 == 0:
            number = number / 2
            round+=1

    if round % 2 == 1:
        return 1
    else:
        return 0

for i in range(0,turn):
    numb = int(input())
    if i % 2 == 0:
        kekik.append(numb)
    else:
        haydarberk.append(numb)

for numberK in kekik:
    kekikP += pointCalc(numberK)

for numberH in haydarberk:
    haydarberkP += pointCalc(numberH)

if haydarberkP < kekikP:
    print("HAYDARBERK")
elif kekikP < haydarberkP:
    print("KEKIK")
else:
    print("DRAW")
