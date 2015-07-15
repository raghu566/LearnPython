_author_='RaghuK'


while 1:
	try:
		x =raw_input("Please enter a number or non-number to exit:")
		x = int(x)
		n = 0
		while x > n:
			n = n + 1
			y = 1
			#print '\n'
			while n >= y:
				print n,
				y = y + 1
		print '\n' + '\n' + 'Booyah Momswy'

		for i in range(1, x+1):
				print str(i) * i
	except:
		break




'''
else:
    print("please input a number")
'''

