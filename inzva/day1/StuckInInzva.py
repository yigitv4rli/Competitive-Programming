def remDup(string):
    length = len(string)
    if length < 2:
        return string

    vowels = ["a","e","i","o","u"]
    result = list()

    index = 0

    while index < length-1:
        letter = string[index]
        nextL = string[index+1]

        if letter in vowels and nextL != letter:
            result.append(letter)
            index+=1

        elif letter in vowels and nextL == letter:
            index+=1
        
        else:
            result.append(letter)
            index +=1

    if nextL not in vowels:
        result.append(nextL)
    elif nextL in vowels and nextL != result[-1]:
        result.append(nextL)

    return ''.join(result)


string = input()
keyword = input()

correctedStr = remDup(string)
correctedKw = remDup(keyword)

if correctedStr.find(correctedKw) != -1:
    print("yes")
else: 
    print("no")
