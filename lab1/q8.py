str="a @#$#@acvcdsf&*^#!@&*%$"

str2=""
for i in range(len(str)):
    if(str[i].isalnum()):str2+=str[i]

print(str2)