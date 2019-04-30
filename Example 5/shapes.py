class Circle:
	def __init__(self,radius):
		self.radius=radius
		self.Pi=22/7

	def area(self):
		A=self.Pi*(self.radius**2)
		print(A)

	def circumference(self):
		C=2*self.Pi*self.radius
		print(C)


class Square:
	def __init__(self,a):
		self.a=a

	def area(self):
		A=self.a**2
		print(A)

	def perimeter(self):
		P=4*self.a
		print(P)

class Rectangle:
	def __init__(self,w,l):
		self.w=w
		self.l=l

	def area(self):
		A=self.w*self.l
		print(A)

	def perimeter(self):
		P=2*(self.l+self.w)
		print(P)


class Sphere:
	def __init__(self,r):
		self.r=r
		self.Pi=22/7

	def surface_area(self):
		A=4*self.Pi*(self.r**2)
		print(A)

	def volume(self):
		V=(4/3)*self.Pi*(self.r**3)
		print(V)
				