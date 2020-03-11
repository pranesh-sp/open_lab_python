class strops:
    def __init__(self):
        self.str=str
    def getString(self):
        self.s=input("enter string:")

    def printstring(self):
        print(self.s.upper())
    def reversestring(self):
        st="".join(reversed(self.s))
        print(str(st))


t=strops()
t.getString()
t.printstring()
t.reversestring()