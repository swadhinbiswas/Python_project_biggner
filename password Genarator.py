import random as ra 

def passgen(n1,n2,n3,n4):
    #cheak the n1 is bigger than len input or not
    if n1>=n2+n3+n4:

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
#password taking
        password=[]
        for _ in range(1,n2+1):
            password.append(ra.choice(letter))

        for i in range(1,n3+1):
            password.append(str(ra.choice(number)))

        for _ in range(1,n4+1):
            password.append(ra.choice(symble))
        ra.shuffle(password)
        return password
    else:
        print("Try again with correct formation")

#input data
n1=int(input("lenth of your password"))
n2=int(input("how many number you want"))
n3=int(input("how many chr you want"))
n4=int(input("how many symble you want"))
#password genarete
passowrd=passgen(n1,n2,n3,n4)
#join string
passwords=''.join(passowrd)
#password print
print(passwords)


