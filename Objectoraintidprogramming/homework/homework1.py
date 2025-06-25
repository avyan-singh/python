import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
  
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        dis=math.sqrt(((y1-y2)**2)-((x1-x2)**2))
        return f"Distance from {self.coor1} to {self.coor2} is {dis} "
    
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        slo=((y1-y2)/(x1-x2))
        return f"Slope of line from {self.coor1} to {self.coor2} is {slo}"
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())
        