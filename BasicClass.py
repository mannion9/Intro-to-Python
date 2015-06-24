class Foo:
    def __init__(self,val):
        self.val = val
    def printVal(self):
        print(self.val)

obj1 = Foo(1)
obj1.printVal()


class vector:
    def __init__(self,vector):
        self.vector = vector
    def dot(vector,vector_new):
        index,results = 0,0
        while index < len(vector):
            result += vector[index]*vector_new[index]
            index += 1
        return result

x = [1,2,3]
