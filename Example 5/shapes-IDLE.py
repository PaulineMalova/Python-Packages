Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Circle:
	def __init__(self,radius):
		self.radius=radius
		self.Pi=22/7

	def area(self):
		A=self.Pi*(self.radius**2)
		print(A)

	def circumference(self):
		C=2*self.Pi*self.radius
		print(C)

		
>>> circle1=Circle(radius=7)
>>> circle1.area()
154.0
>>> circle1.circumference()
44.0
>>> circle2=Circle(radius=20)
>>> circle2.area()
1257.142857142857
>>> circle2.circumference()
125.71428571428571
>>> 
>>> 
>>> class Square:
	def __init__(self,a):
		self.a=a

	def area(self):
		A=self.a**2
		print(A)

	def perimeter(self):
		P=4*self.a
		print(P)

		
>>> square1=Square(a=5)
>>> square1.area()
25
>>> square1.perimeter()
20
>>> square2=Square(a=40)
>>> square2.area()
1600
>>> square2.perimeter()
160
>>> 
>>> 
>>> class Rectangle:
	def __init__(self,w,l):
		self.w=w
		self.l=l

	def area(self):
		A=self.w*self.l
		print(A)

	def perimeter(self):
		P=2*(self.l+self.w)
		print(P)

		
>>> rectangle1=Rectangle(w=7,l=9)
>>> rectangle1.area()
63
>>> rectangle1.perimeter()
32
>>> rectangle2=Rectangle(w=40,l=30)
>>> rectangle2.area()
1200
>>> rectangle2.perimeter()
140
>>> 
>>> 
>>> class Sphere:
	def __init__(self,r):
		self.r=r
		self.Pi=22/7

	def surface_area(self):
		A=4*self.Pi*(self.r**2)
		print(A)

	def volume(self):
		V=(4/3)*self.Pi*(self.r**3)
		print(V)

		
>>> sphere1=Sphere(r=7)
>>> sphere1.surface_area()
616.0
>>> sphere1.volume()
1437.333333333333
>>> sphere2=Sphere(r=21)
>>> sphere2.surface_area()
5544.0
>>> sphere2.volume()
38807.99999999999
>>> 
