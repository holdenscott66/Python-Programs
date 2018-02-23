#Scott Holden - completed all parts of assignment

def startup():	#function that sets up the game
	print("Welcome to the game of nuts!")
	n = int(input('How many nuts are there on the table initially (10-100)? ')) #n is the number of nuts that will be on the table
	table = hats_func(n) #calls hat function, creates table with n hats
	while n > 100 or n < 10: #if n is not in the range 10-100
		print('Please enter a number between 10 and 100')
		n = int(input('How many nuts are there on the table initially (10-100)? '))
	print('Options: \n Play against a friend (1) \n Play against the computer (2) \n Play against a trained computer (3)') #prints game options
	opt = str(input('Which option do you take (1-3)?')) #input for user to choose game
	if opt == '1':
		human_human(n) #calls function for human vs human
	elif opt == '2':
		play_again(n,table) #calls function that calls human vs ai function, and repeats as long as user wants
	elif opt == '3':
		print('Training AI, please wait...')
		table = train(n) #calls train function and assigns it to variable table. 
		play_again(n,table) #calls function that calls huan vs ai function. using table after 100000 games. 
		print(table) #prints table of the trained ai vs human, used for testing
		
def hats_func(startnuts): #defines function, with parameter startnuts. Creates table based on number of nuts at beginning of game
	hats = [] 
	for i in range(startnuts): 
		row = [1, 1, 1] 
		hats += [row]
	# print(hats)
	return hats	
	
def select(p): #function give in assignment outline, determines how many nuts ai will take based on integers in a specific list
 # assumes p is a list of three positive integers
	import random
	total = p[0] + p[1] + p[2]
	r_int = random.randint(1, total) 
	if (r_int <= p[0]): 
		move = 0 
	elif (r_int <= p[0] + p[1]): 
		move = 1 
	else: move = 2 
	return move	
	
def human_turn(plyr, nuts): #defines function for human turn, parameter is which player, and how many nuts are on the table
	print()
	if nuts > 1:
		print('There are {} nuts on the board.'.format(nuts))
	elif nuts == 1:
		print('There is 1 nut on the board.')
	lessnuts = int(input('Player {}: How many nuts do you take (1-3)? '.format(plyr))) #lessnuts is the amount of nuts that are taken off of the table
	while lessnuts < 1 or lessnuts > 3: #if input is not in 1-3 it will ask for new input
			print('Please enter a number between 1 and 3')
			lessnuts = int(input('Player {}: How many nuts do you take (1-3)? '.format(plyr)))
	nuts = nuts - lessnuts #number of nuts left on the table
	return nuts
		
def human_human(startnuts): #defines function for human vs human, parameter is number of nuts at the start of the game
	nuts = startnuts
	while nuts >=1: #while there is 1 or more nuts left
		for plyr in (1,2): #uses for loop to call human_turn function, alternating between plyr 1 and 2
			nuts = human_turn(plyr,nuts) #new value of nuts is the return of the function human_turn
			if nuts < 1:
				print('Player {}, you lose.'.format(plyr)) #ends game if there is no nuts left.
				break
				
def play_again(n, table): #defines function. n is number of nuts on table, table is the table that determines how many nuts ai will take
	while True: #executes while true
		human_ai(n, table) #calls function that plays human vs ai
		again = str(input('Play again (1 = yes, 0 = no)?'))
		if again == '1': #continues loop if input is 1
			continue
		# print(table) #prints table after game is over, used to test
		break	#exits while loop 
		
def human_ai(startnuts, table): #defines function for human vs ai. Either trained or untrained dependant on which table is used. 
	nuts = startnuts
	newtable = [] #creates empty list
	while nuts >= 1:
		nuts = human_turn(1,nuts) #calls function, parameter plyr is assigned value of 1 so only player 1 is playing
		if nuts < 1:
			print('Player 1, you lose.')
			table = ai_win(table, newtable) #if ai wins, it updates the table accordingly
			# print(table) #used to check table after each game
			return table		
		nuts, newtable = ai_turn(nuts, table, newtable) #calls function of ai_turn, returns values of nuts and the newtable
		if nuts < 1:
			print('AI loses.')
			table = ai_loss(table, newtable) #if ai loses, table is updated accordingly
			# print(table)#used to check table after each game
			return table
			
def ai_win(table, newtable): #defines function for updating the table of hats if ai wins. Parameters are the original table, and values in the newtable
	for x,y in newtable: #newtable is nested list, takes indexes in each sublist which are based on the number of nuts that the ai took
		z = table[x][y] #determines index of value based on the sublist in newtable
		table[x][y] = z + 1 #updates value at the according index
	return table

def ai_loss(table, newtable): #defines function for updating table of hats if ai loses.
	for x,y in newtable:
		z = table[x][y]
		if z > 1: #if the values in the hat are greater than 1
			table[x][y] = z - 1 #value at specified index will be less 1 
	return table

def ai_turn(nuts, table, newtable): #defines function for the ai's turn, parameters are nuts, the table of hats, and the empty list
	print()
	if nuts > 1:
		print('There are {} nuts on the board.'.format(nuts))
	elif nuts == 1:
		print('There is 1 nut on the board.')
	lessnuts = select(table[nuts - 1]) #calls function select at value of table at index nuts - 1. nuts - 1 because the index is one less than the value
	newtable.append([nuts - 1, lessnuts]) #appends index of nuts, and nuts that ai takes as sublist.
	nuts = nuts - (lessnuts + 1) #determines new value of nuts on table
	print('AI selects {}'.format(lessnuts + 1))
	# print(newtable) #used to check values in table
	return nuts, newtable
	
def ai_1(nuts, table, newtable): # function used for ai turn when training the ai
	lessnuts = select(table[nuts - 1])
	newtable.append([nuts - 1, lessnuts])
	nuts = nuts - (lessnuts + 1)
	# print(newtable)
	return nuts, newtable
	
def train(nuts): #calls function 100000 times and continues to update the values in table
	table = hats_func(nuts)
	for i in range(100000):
		battle(nuts, table)
	return table
			
def battle(nuts, table): #function for playing 1 ai against another, updates list for each ai, the winning list is used to change values in table 
	newtable1 = []
	newtable2 = []
	while nuts >= 1:
		nuts, newtable1 = ai_1(nuts, table, newtable1)
		if nuts < 1:
			table = ai_win(table, newtable2)
			# print(table)
			return table
		nuts, newtable2 = ai_1(nuts, table, newtable2)
		if nuts < 1:
			table = ai_win(table, newtable1)
			# print(table)
			return table
			
startup()