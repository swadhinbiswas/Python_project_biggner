import random as ra 
# asking for guess len

try:
    n=int(input("input your guess len : "))

except(ValueError):
    print("You Must have to input Int Value")

randomvalue=ra.randrange(0,n)

#randomvalue=ra.randrange(0,n)
guesses=0

while True:
    guesses+=1
    #make sure programe will run if the user input not int value
    try:
        user_input=int(input())
        if user_input==randomvalue:
            print("You got it bro with guesses",guesses)
            break
        elif guesses<n-1:
            #if user inter wrong guess
            print("You get is wrong Bro!")
            continue
        else:
           print("You loose!!!kido")
           print("Right value was",randomvalue)
           break
# Trying to not destroying programme if input not Int value 
    except(ValueError):
        print("Only Int is accepectable")
