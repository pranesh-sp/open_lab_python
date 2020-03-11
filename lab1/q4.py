st="Hello World"
u=0;
l=0
for i in st:
    if(i.isupper()):u+=1;
    if(i.islower()):l+=1;

print("no of uppers:"+str(u) + "  \nno of lowers : "+ str(l))