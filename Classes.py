class Point:
    ''' The "__init__(self,*other)" function initializes all variables
        that will be used in the class, it essentially makes the object '''
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    ''' When we print an instance of this class, we get a messy format of the
        form "<__main__.Point object at 0x00000000031F8CC0>" which is not helpful
        and so we can write a special function that will indicate how we want
        to print the instance '''
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    ''' Now there are special features you can give objects, such as when ever
        you add or multply two objects of the same class, the object has a special
        built in function that says what to do, which makes writing codes easier.
        There are a bunch of these "Overload" functions you can look up. They all
        start with a "__" and end with a "__" like the __init__ and __str__ functions.'''
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x,y)
    
    


# Create the Point object called p1
p1 = Point(1,3)
p2 = Point(1,1)
# Print in the format we have designed
print(p1)
print(p2)
# Use the "__add__" function
p3 = p1 + p2
print(p3)
# Use the "__mul__" function
p4 = p1 * p2
print(p4)



