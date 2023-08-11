email=input("input your mail adress  :  ")
j,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email)and(email.count("@")==1):
            if(email[-4]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1 
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                        elif i=="_":
                            continue
                        else:
                            d=1
                if k==1 and j==1 and k==1:
                    print("wrong mail")
                else:
                    print("Right mail")

else:
    print("Wrong mail ")



    

                    