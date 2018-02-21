#Scott Holden 30051473
import turtle #import turtle module
import random #import random module

def setup_Alice(turtle1,xmin,xmax,ymin,ymax): #defines the function for setting up turtle1- whcih will later be assigned to Alice 
	turtle1.color('red') #changes color to red
	turtle1.shape('turtle') #changes shape to a turtle
	rndx = random.randint(xmin,xmax) #generates random integer to be used as x coordinate
	rndy = random.randint(ymin,ymax) #generates random integer to be used as y coordinate
	turtle1.penup() #lifts pen so no marks are made
	turtle1.setpos(rndx, rndy) #moves turtle1 to random position, using rndx,rndy coordinates
	turtle1.pendown() #puts pen down so mrks will be made

def setup_Alex(turtle2): #defines the function for setting up turtle2- which will later be assigned to Alex
	turtle2.color('blue') #sets color to blue
	turtle2.shape('turtle') #changes shape to a turtle
	
def setup_stats(turtle3,xmin, ymax):	#sets up turtle3- which will later be assigned to stats
	turtle3.penup() #lifts pen so no marks are made
	turtle3.ht() #makes turtle3 invisible
	turtle3.setposition(xmin + 10,ymax - 20) #moves turtle3 to top left of screen

def main_setup(turtle1, turtle2, turtle3,xmin,xmax,ymin,ymax): #defines function for setting up the turtle window
	turtle.Screen() #creates window
	turtle.Screen().setworldcoordinates(xmin,ymin,xmax,ymax) #creates screen, defined by parameters
	turtle.Screen().title("Assignment 2- Chasing Alice") # sets title at top of screen 
	setup_Alice(turtle1, xmin,xmax,ymin,ymax) #calls function to setup turtle1
	setup_Alex(turtle2)#calls function to setup turtle2
	setup_stats(turtle3,xmin,ymax)#calls function to setup turtle3
	
def Alex_turn(turtle2, alexdistance, alexangle): #defines what turtle2 does for each of his turns
	prompt = str(input("Enter direction Alex will move:")) #input prompt, changes type to string
	while prompt not in "wasd":#if input is not w,a,s, or d message is printed nd user is prompted to input again
		print("my_string is not recognized as a movement.retype")
		prompt = str(input("Enter direction Alex will move:"))
	if prompt == 'w' : #if w is entered, turtle2 moves forward
		turtle2.forward(alexdistance)
	elif prompt == 'a' :# if a is entered, he turns left
		turtle2.left(alexangle)
	elif prompt == 's' :# if s is entered, he goes back
		turtle2.backward(alexdistance)
	elif prompt == 'd' : #if d is entered. he turns right
		turtle2.right(alexangle)
		
def Alice_turn(turtle1, alicedistance, aliceangle):#defines what turtle2 does for each turn, Alice will be used as the paramter when she has been defined
	Alice_rnd = random.randint(0,2)#generates random integer 0,1 or 2 -- 
	if Alice_rnd == 0: #if Alice_rnd is 0 (1/3) chance-- it proceeds
		left_right = random.randint(0,1) #generates random integer, 0 or 1
		if left_right == 0: #if random integer is 0, turtle1 turns left
			turtle1.left(aliceangle)
		else :#if random integer is not zero, turtle1 turns right
			turtle1.right(aliceangle)
	else:#if Alice_rnd is not zero, it is either 1 or 2 (2/3) chance, turtle1 moves forward
		turtle1.forward(alicedistance)

def turtle_reset(turtlex,xmin,xmax,ymin,ymax): #defines function of what happens when a turtle goes off of the screen
	posx, posy = turtlex.position() #returns turtle (yet to be assigned) position as coordinates (posx,posy)
	if not (xmin < posx < xmax and ymin < posy < ymax) : #if turtles coordinates are not within the window
		newx = random.randint(xmin, xmax) #generates random integer, assigns to x 
		newy = random.randint(ymin, ymax) #generates random integer assigns to y
		turtlex.setposition(newx,newy) #sets turtle's position to x,y (random location)
		
def stats_update(turtle3, step, distance): # defines function for updating statistics, parameters step, distance, and turtle3
	turtle3.clear() #clears the previous statistics written
	turtle3.write("Step#: "+ str(step) + " Distance between Alice and Alex: {0:.2f}".format(distance))	#write out the stats, (step) will be int, gets converted to string. {0:.2f}".format(distance)--> writes distance to 2 decimal places.

def taking_turns(turtle1, turtle2, turtle3,alexdistance,alexangle,alicedistance,aliceangle,xmin,xmax,ymin,ymax): #defines function for executing Alex's turn, Alice's turn, and updating the stats. Also for turtle_reset.
	count = 1	#sets count to 1 
	dist = turtle2.distance(turtle1)#returns the distance between Alex and Alice from any direction. 
	stats_update(turtle3, count, dist)#updates stats, count and dist have been defined but turtle3 has not yet been defined.
	while dist > 30: #while loop, executes following while distance between turtles 1 and 2 is more than 30
		Alex_turn(turtle2,alexdistance,alexangle) #executes function Alex_turn()
		turtle_reset(turtle2,xmin,xmax,ymin,ymax) #checks to see if turtle2 is on the screen, if yes, nothing happens, if no, he is moved to random location
		Alice_turn(turtle1,alicedistance,aliceangle) #executes function Alice_turn()
		turtle_reset(turtle1,xmin,xmax,ymin,ymax) #checks turtle1's location, moves her if necessary
		count += 1 #for each iteration the value of count increases by 1
		dist = turtle2.distance(turtle1) #returns the distance between turtles 1 and 2 after each iteration
		stats_update(turtle3,count, dist)# updates stats at the top of screen with turtle 3, count and dist 
		
def main(): #defines the main function which will call all necessary functions and assign all parameters
	Alice = turtle.Turtle() #creates turtle and defines as Alice
	Alex = turtle.Turtle() #creates turtle and defines as Alex
	stats = turtle.Turtle() #creates turtle and defines as stats
	alexdistance= 30 #sets alex distance to 30
	alexangle= 45 #sets angle he will turn to 45
	alicedistance= 20 #sets distance alice will move to 20
	aliceangle= 90 #sets angle she will turn to 90
	xmin = -250 #defines the height and width of the window, 0,0 at centre
	xmax = 250
	ymin = -250
	ymax = 250
	main_setup(Alice,Alex,stats, xmin,xmax,ymin,ymax)#calls function 
	taking_turns(Alice,Alex,stats,alexdistance,alexangle,alicedistance,aliceangle,xmin,xmax,ymin,ymax)
	turtle.Screen().mainloop() #keeps window open after Alex has caught Alice
	
main()