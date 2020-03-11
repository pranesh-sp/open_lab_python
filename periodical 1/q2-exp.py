class date(object):

    def __init__(self, day, month, year):
            self.day=int(day)
            self.month=int(month)
            self.year=int(year)
    #overloading the -
    def __sub__(self, other):
        return self.year - other.year, self.month - other.month, self.day - other.day

print("enter date of joining :")
doj=date(input("enter day: "),input("enter month: "),input("enter year: "))
print(doj.day," ",doj.month," ", doj.year)

print("enter current date :")
cur_date=date(input("enter day: "),input("enter month: "),input("enter year: "))
print(cur_date.day," ",cur_date.month," ", cur_date.year)

exp=cur_date-doj

print("experience = ", exp[2], "days", exp[1], "months", exp[0], "years")







