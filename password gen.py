import random as ra

letter=[]
        #makking the list of alfabet
letter=list(map(chr, range(65,91)))
        #list of small leter alfabet
smlatter=list(map(chr, range(97,122)))
#appending the small letter into letter list
for x in range(len(smlatter)):
    letter.append(smlatter[x])
#make number list
number=list(map(int,range(0,10)))
    #make symble list
symble=list(map(chr,range(33,65)))
        #appending all the symble in symble list
symble.append(list(map(chr,range(91,97))))
symble.append(list(map(chr,range(123,127))))




n=int(input())
n2=int(input())
n3=int(input())
#password taking
password=[]
for x in range(1,n):
    password.append(ra.choice(letter))

for _ in range(1,n2):
    password.append(str(ra.choice(number)))

for _ in range(1,n3):
    password.append(ra.choice(symble))


ra.shuffle(password)


#passwords=''.join(passowrd)
print(password)


