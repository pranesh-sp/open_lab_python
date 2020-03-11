class circle:
    def __init__(self,radius):
        self.radius=radius

    def computeArea(self):
        area=3.14*self.radius*self.radius
        return area
    def computeCircu(self):
        cir=2*3.14*self.radius
        return cir


p1=circle(25)
print(p1.computeArea())
print( p1.computeCircu())
