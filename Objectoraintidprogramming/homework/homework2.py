from math import pi

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        vol=pi * self.radius * self.radius * self.height
        return f"Volume of following cylinder is {vol}"
    
    def surface_area(self):
        area=(2 * pi * self.radius * self.radius) + (2 * pi * self.radius * self.height)
        return f"area of following cylinder is {area}"

HEIGHT=int(input("height should be: "))
RADIUS=int(input("radius should be: "))

cylinder= Cylinder(HEIGHT,RADIUS)

print(cylinder.volume())
print(cylinder.surface_area())