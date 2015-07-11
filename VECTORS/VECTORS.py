class Vector:
    ''' Vector of unknown length. Inputs is a list. '''
    def __init__(self,r):
        self.r = r
    def __len__(self):
        ''' Returns length of vector. '''
        '''Ex: len(Vector([1,2])) '''
        return (len(self.r))
    def __getitem__(self,key):
        ''' Returns element in vector. '''
        '''Ex: Vector([1,2])[0] '''
        return self.r[key]
    def __setitem__(self,key,value):
        ''' Sets element in vector to a value.'''
        '''Ex: Vector([1,2])[0]=3'''
        if key < len(self.r):
            self.r[key]=value
        if key == len(self.r):
            self.r.append(value)
        else:
            raise IndexError('Invalid index key')
    def __repr__(self):
        ''' Returns a string version of vector.'''
        '''Ex: x=Vector([1,2]) ... x---> Vector [1,2]'''
        return 'Vector %s' % self.r
    def __add__(self,other):
        ''' Returns the addition, allows other to be vector or a int/float'''
        ''' Ex: (x is vectors, y is vector/int/float) z = x+y '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i] + other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i] + other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector,float, or int')
    def __radd__(self,other):
        ''' Returns the addition, allows other to be vector or a int/float'''
        ''' Ex: (x is vectors, y is vector/int/float) z = x+y '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i] + other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i] + other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector,float, or int')
    def __iadd__(self,other):
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i] + other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i] + other for i in range(len(self.r))])
    def __sub__(self,other):
        ''' Returns the addition, allows other to be vector or a int/float'''
        ''' Ex: (x is vectors, y is vector/int/float) z = x-y '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i] - other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i] - other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector,list,float, or int')
    def __rsub__(self,other):
        ''' Returns the addition, allows other to be vector or a int/float'''
        ''' Ex: (x is vectors, y is vector/int/float) z = x-y '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([other[i] - self.r[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([other - self.r[i] for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector,list,float, or int')
    def __isub__(self,other):
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i] - other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i] - other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector,list,float, or int')
    def __mul__(self,other):
        ''' Returns the element by element mulutiplication'''
        ''' x*y = z '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i]*other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i]*other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __rmul__(self,other):
        ''' Returns the element by element mulutiplication'''
        ''' x*y = z '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i]*other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i]*other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __imul__(self,other):
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i]*other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i]*other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __truediv__(self,other):
        ''' Returns the element by element division'''
        ''' x.divide(y) = z '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i]/other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i]/other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __rtruediv__(self,other):
        ''' Returns the element by element division'''
        ''' x.divide(y) = z '''
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([other[i]/self.r[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([other/self.r[i] for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __itruediv__(self,other):
        if isinstance(other,Vector) or isinstance(other,list):
            return Vector([self.r[i]/other[i] for i in range(len(self.r))])
        if isinstance(other,float) or isinstance(other,int):
            return Vector([self.r[i]/other for i in range(len(self.r))])
        else:
            raise TypeError('other must be Vector or list')
    def __pow__(self,power):
        ''' Returns the vector raised to a power '''
        ''' Ex: x.pow(2) '''
        assert type(power) == int or type(power) == float, 'Must be raised to a int or float'
        return Vector([self.r[i]**power for i in range(len(self.r))])
    def average(self):
        ''' Returns average of vector elements'''
        ''' Ex: x.averager() '''
        return sum(self.r)/len(self.r)
    def norm(self):
        ''' Returns norm of vector'''
        ''' Ex: x.norm() '''
        return (sum([self.r[i]*self.r[i] for i in range(len(self.r))]))**(1/2)

    


