#Kaleb Soule Lab 03

#Create Classes
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    
class Cirlce(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height
    
#Read Txt File
file = open(r'C:\Users\Owner\OneDrive\Documents\GitHub\Soule-online-GEOG676-spring2025\LAB3\shape.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of Rectangle is:', rect.getArea())
    elif shape == 'Circle':
        cirl = Cirlce(int(components[1]))
        print('Area of Circle is:', cirl.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of Triangle is:', tri.getArea())
    else:
        pass



# Example for Separating Lines
# tamu = "Texas A&M University"

# tokens = tamu.split(" ") # We split our string on whitespace
# print(len(tokens)) # Prints 3 since we have three components
# print(tokens) # Prints ["Texas", "A&M", "University"]