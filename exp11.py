class polygon:
    def area(self,base,height):
        return .5*base*height
    
class triangle(polygon):
    pass

t=triangle()
b=float(input('Enter the base:'))
h=float(input('Enter the height:'))
area=t.area(b,h)
print("the area of teh triangle is :",area)