import random

def human_human(startnuts):
	numnuts = startnuts
	while numnuts != -1:
		for plyr in (1,2):
			print()
			if numnuts != 1:
				print('There are {} nuts on the board.'.format(numnuts))
			elif numnuts == 1:
				print('There is 1 nut on the board.')
			lessnuts = int(input('Player {}: How many nuts do you take (1-3)? '.format(plyr)))
			while lessnuts < 1 or lessnuts > 3:
					print('Please enter a number between 1 and 3')
					lessnuts = int(input('Player {}: How many nuts do you take (1-3)? '.format(plyr)))
			numnuts = numnuts - lessnuts
			if numnuts < 1:
				print('Player {}, you lose.'.format(plyr))
				numnuts = -1
				
def hats_func(numnuts):			
	hats = [] 
	for i in range(numnuts): 
		row = [1, 1, 1] 
		hats += [row]
	print(hats)
	
def select(p):
 # assumes p is a list of three positive integers
	total = p[0] + p[1] + p[2]
	r_int = random.randint(1, total) 
	if (r_int <= p[0]): 
		move = 0 
	elif (r_int <= p[0] + p[1]): 
		move = 1 
	else: move = 2 
	return move
	
def human_ai(startnuts):
	hats_func(startnuts)
		
def startup():	
	print("Welcome to the game of nuts!")
	numnuts = int(input('How many nuts are there on the table initially (10-100)? '))
	while numnuts > 100 or numnuts < 10:
		print('Please enter a number between 10 and 100')
		numnuts = int(input('How many nuts are there on the table initially (10-100)? '))
	print('Options: \n Play against a friend (1) \n Play against the computer (2) \n Play against a trained computer (3)')
	opt = int(input('Which option do you take (1-3)?'))
	if opt == 1:
		human_human(numnuts)
	# elif opt == 2:
		# human_ai()
	# elif opt == 3:
		# human_train()
startup()
