email= input("enter your email : ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j == 1 or d == 1:
                    print("wrong email:check again ")
            else:
                print("wrong email: .com or .in should be there")
        else:
            print("wrong email: its seems @ is missing")
    else:
        print("wrong email error: 1 letter should be capital")
else:
    print("wrong email error: too small, min 26 character needed")