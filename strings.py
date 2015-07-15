__author__ = 'RajK'

me = raw_input("Enter your name:" )
friend =raw_input("Enter friend's name: ")
time = '{}'.format(raw_input("Enter the meeting time: "))
print(friend + ' will meet ' + me + ' at ' + time +'.')
print(friend, ' will meet ', me, ' at ', time)
print('{} will interview {} at {}.'.format(friend, me, time))
