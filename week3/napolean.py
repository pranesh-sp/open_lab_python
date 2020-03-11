s=int(input())

x=0
while(x<s):
    ar = input().split()

    buildings = input().split()

    n = ar[0]
    r = ar[1]
    amt = []
    cost=0;
    if(buildings!=""):
        max = int(buildings[0])
        cost=int(r)


    for j in range(int(n)):
        if(max<int(buildings[j])):
            max=int(buildings[j])
            j+=1
            cost+=int(r);


    print(cost)
    cost=0
    x+=1