_author_='RaghuK'


x =raw_input("What shape are you choosing? Square,Circle,or a Triangle. Type your answer:")
if x== "Square":
	y =raw_input("What is the length of one side of your square. Type your answer:")
	y = int(y)
	Perimeter = y*4
	Area = (y*y)
	print "The perimeter of your square is", Perimeter
	print "The area of your square is", Area
	
if x== "Circle":
	z =raw_input("What is the radius your circle. Type your answer:")
	z = int(z)
	Circumference = 2*z*3.14
	Area = z*z*3.14
	print "The approximate circumference of your circle is", Circumference
	print "The approximate area of your circle is", Area
	
if x== "Triangle":
	v =raw_input("What is the length of your hypotenuse:")
	w =raw_input("What is the length of one altitude on your triangle:")
	f =raw_input("What is the length of the other altitude on your triangle:")
	v = int(v)
	w = int(w)
	f = int(w)
	Area = f*w/2
	Perimeter = v+w+f
	print "The perimeter of your triangle is", Perimeter
	print "The area of your triangle is", Area
