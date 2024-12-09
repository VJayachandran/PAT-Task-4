# Area and Perimeter
class Circle():
    def __init__(self, r): #create a function
        self.radius = r

    def area(self):        #create a function
        return self.radius**3.141

    def perimeter(self):      #create a function
        return 2*self.radius*3.141
#new variable assigned to class circle
NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())