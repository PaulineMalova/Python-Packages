def tens():
	num_list = [1,2,3,4,5,6,7,8,9]
	for x in num_list:
		y = x*10
		print (y)

def squares():
	num_list = [2,4,6,8,10,12]
	w = [x**2 for x in num_list]
	print(w)

def sorted():
	a = [9,1,4,7,3]
	b = [5,2,6,8,0]
	c = a+b
	c.sort()
	print (c)

def range_sum(n):
	f = []
	for x in range(1,n+1):
		f.append(x)
		ans = sum(f)
	print (ans)	

def largest(m):
	print (max(m))

def smallest(p):
	print (min(p))	

def my_modulus():
	h = dict()
	j = range(10,20)
	for x in j:
		h[x] = x%3
	return (h)	

def print_dict():
	students = [{'balance':1000, 'name':'Irene'},{'balance':2000,'name':'Pauline'},{'balance':3000,'name':'Naima'},{'balance':1000,'name':'Rose'}]
	for student in students:
		print("Hello {}, your balance is {}.".format(student['name'],student['balance']))					