class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def getCircumference(self):
        return 2 * Circle.pi * self.radius
    def getArea(self):
        return Circle.pi * Circle.pi * self.radius
mycircle=Circle(1)
print(mycircle.getCircumference())
print(mycircle.getArea())
        

        