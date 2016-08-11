vector mathematics:
import math
class class_vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.v=(x,y)
    def __str__(self):
        return "("+str(x)+","+str(y)+")"
    def __add__(self):
        return [i+j for (i,j) in zip(self.v,self.v)]
    def __sub__(self):
        return [i-j for (i,j) in zip(self.v,self.v)]
    def __mul__(self):
        return sum([i*j for (i,j) in zip(self.v,self.v)])
    def __magitude__(self):
        return math.sqrt(self.x**2+self.y**2)
x=int(raw_input("Enter x value: "))
y=int(raw_input("Enter y value: "))
obj_vector=class_vector(x,y)
print "Vector: ",obj_vector.__str__()
print "adittion of vectors (",x,y,"),(",x,y,"): ",obj_vector.__add__()
print "Substraction of vectors (",x,y,"),(",x,y,"): ",obj_vector.__sub__()
print "Multiplication of vectors (",x,y,"),(",x,y,"): ",obj_vector.__mul__()
print "Magnitude of vector (",x,y,"): ",obj_vector.__magitude__()
