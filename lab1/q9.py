uname=input("username:\n")
pwd=input("pass : \n")
un=0;
if(uname.isalnum()):un=1;
else:print("uname not valid")



l=len(pwd)
sym=0;
lc=0;
uc=0;
for i in pwd:

    if(i.islower()):lc+=1;
    if(i.isupper()):lc+=1;
    if(i.isalnum()==False):sym+=1;

if(un==1):print("username valid")


if(l==8 and sym>0 and lc>0 and uc>0 ):print("password valid")
else: print("password not valid")