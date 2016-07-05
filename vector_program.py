# importign math module to do sqrt
import math
# class declaration
class class_vector():
	'''
	class is to define a vector and provide methods to do vector adittion and substraction and magnitude
	'''
	def __init__(self,x,y):
		'''
		constructor of the class which can call automatically while creating an object of the class
		'''
		self.x=x
		self.y=y
		self.v=(x,y)
	def __str__(self):
		'''
		this method used to define object in string format
		'''
		return "("+str(self.x)+","+str(self.y)+")"
	def __add__(self):
		'''
		method to add two vectors
		'''
		add_l=[]
		ind=0
		for i in self.v:
			add_l.append(i+self.v[ind])
			ind=ind+1
		return add_l
	def __sub__(self):
		'''
		methos to substract two vectors
		'''
		sub_l=[]
		ind=0
		for i in self.v:
			sub_l.append(i-self.v[ind])
			ind=ind+1
		return sub_l
	def __mul__(self):
		'''
		method to multiply two vectors and returns the result
		'''
		mul_l=[]
		ind=0
		for i in self.v:
			mul_l.append(i*self.v[ind])
			ind=ind+1
		return mul_l
	def __magnitude__(self):
		'''
		method to find magnitude of the given vector
		'''
		return math.sqrt(self.x**2+self.y**2)
x1=raw_input("value x1: ") # get x1 value from the user
x1=int(x1) # convert x1 vale to int type
x2=raw_input("value x2: ") # get x2 value from the user
x2=int(x2) # convert x2 to int type
obj_vector=class_vector(x1,x2) #  creating an object to make a vector
v1=obj_vector.__str__() # calling __str__ method to convert object to String format of the vector
print "Vector: ",v1 # printing vector
v1_add= obj_vector.__add__() # calling __add__ method
print "adittion of (",x1,x2,"),(",x1,x2,"): ", v1_add # printing additiion of vectors
v1_sub= obj_vector.__sub__() # calling __sub__ method
print "Substraction of (",x1,x2,"),(",x1,x2,"): ", v1_sub # printing substraction of the vector 
v1_mul= obj_vector.__mul__() # calling __mul__ method
print "Multiplication of (",x1,x2,"),(",x1,x2,"): ", v1_mul # printing multiplication of the vector
v1_mag= obj_vector.__magnitude__() # calling __magnitude__ method
print "Magnitude of (",x1,x2,"): ", v1_mag # printing magnitude of the vector..



		
