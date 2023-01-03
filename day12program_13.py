class Rectangle:
    
    def __init__(self,breadth,length):
        self.length=length
        self.breadth=breadth
    def calculateArea(self):
        temp=self.length*self.breadth
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.breadth)
        return temp
l=int(input('length:'))
b=int(input('breadth:'))


ob=Rectangle(l,b)
area=ob.calculateArea()
peri=ob.calculatePerimeter()
print('Area of rectangle:',area)
print('perimeter of rectangle',peri)

