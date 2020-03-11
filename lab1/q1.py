str=input("enter string to capitalize:")
i=0
while(i<len(str)):
    if(str[i]==" "):
        print(str[i+1])
        str[i+1].upper();

    i+=1;

print(str)