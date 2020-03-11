class find:
    def __init__(self,num):
        self.num=num
    def fin(self):
        n=input("enter target number: ")
        for i in range(len(num)):

            for j in range(len(num)):

                if(int(n)==i+j):

                    s="indices are " + str(i) +" and element = "+ str(num[i]) + "\n and " + str(j) + " and element = "+ str(num[i])
                    print(s)

num = [3,2,1]

11
t=find(num)
t.fin()
