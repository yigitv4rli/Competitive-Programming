import string
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

coming = list()
for line in fin.readlines():
    coming.append(line.rstrip())
x = coming[0]
y = coming[1]


letters = dict()
num = 1
for key in string.ascii_uppercase:
    letters[key] = num
    num+=1

s1, s2 = 1, 1

for char in x:
    s1 *= letters[char]

for char in y:
    s2 *= letters[char]

if s1 % 47 == s2 % 47:
    fout.write ('GO' + '\n')
    fout.close()    
else:
    fout.write ('STAY' + '\n')
    fout.close()    
