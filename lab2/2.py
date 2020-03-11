class time():
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def addTime(t1,t2):
        t3 = time(0, 0)
        if t1.mins + t2.mins > 60:
            t3.hours = (t1.mins + t2.mins) / 60
        t3.hours = t3.hours + t1.hours + t2.hours
        t3.mins = (t1.mins + t2.mins) - (((t1.mins + t2.mins) / 60) * 60)
        return t3
    def showTime(self):
        s=str(self.hours) + "hours and " + str(self.mins) +" mins"
        print(s)

    def showMin(self):
        m=self.mins+self.hours*60
        print(m)

t1=time(2,19)
t2=time(2,1)
t3=time.addTime(t1,t2)
print(t3.hours,t3.mins)
t1.showTime()
t2.showMin()