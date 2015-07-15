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
	h =raw_input("What is the length of your hypotenuse:")
	l =raw_input("What is the length on your triangle:")
	w =raw_input("What is the width on your triangle:")
	ih = int(h)
	il = int(l)
	iw = int(w)
	Area = (il*iw)/2
	Perimeter = ih+iw+il
	print "The perimeter of your triangle is", Perimeter
	print "The area of your triangle is", Area

