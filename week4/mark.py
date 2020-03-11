n=int(input())
ls=input().split()
k=0
s=""

for i in ls:
    for j in ls[k:]:
        if(int(i)<int(j)):ls[k]=0
    k+=1
for i in ls:
    if(i!=0):
        s+=str(i)+  " "

print(s)
