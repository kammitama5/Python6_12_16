##Welcome message --> game begin

print 'Welcome to my game. This game is sweet.'
##ask the player for his name
player_name = raw_input('What\'s is your name: ')

## check/ask for player name and display it
if player_name == '':
	print'\n'
	print 'You entered an empty string!'
else:
	
	print 'Your name is {}'.format(player_name)

## check/ask for player age and display it
page =  raw_input('What is your age: ')
if page.isdigit():
	page = int(page)
	print 'Your age is {}'.format(page)
	print'\n'
else:
	print 'Not a real age'
	print'\n'

## functions for gamestuff values of dragon, mazes, dungeons or the single life
def do_dragons():
	print'\n'
	print 'Rahhhh dragons'
	print'\n'
	
	lim = 5
	dragon_hp = 100
	
	import random
	
	for x in range(lim):
		hit = random.randint(0,100)
		dragon_hp -= hit
		if dragon_hp > 0:
			print '\n'
			print 'You hit for {} damage! Dragon HP at {}!'.format(hit, dragon_hp)
			print '\n'
			print 'You killed him! YOU MONSTER!'
			print '\n'
			print 'GAME OVER!'
			import sys
			sys.exit()
			print '\n'
		else:
			print '\n'	
			print 'You failed to kill the dragon. Scrub.'
		return 0
	
def do_mazes():
	print'\n'
	print 'Wheee! you are in a maze!'
	print'\n'
	
	maze_answer = raw_input('Would you like to find your way out? ')

## want to play in maze?
	if maze_answer == 'yes':
			print 'You are now out of the maze. That was fun, huh?'
			print '\n'
			return 0
	else:
			print '\n'
			print 'You are still stuck in the maze. Are you scared?'
			print '\n'
			print 'Whoops...do not go there...I said...what..is..wrong..with you?'
			print '\n'
			print 'Oh no...you just took a wrong turn!'
			print '\n'
			print 'GAME OVER'
			import sys
			sys.exit()
		
def do_secret():
	print '\n'
	
	secret = raw_input('Choose a secret item: 1, 2 or 3... ')
	
	if secret.isdigit():
		secret = int(secret)
		print '\n'
		print 'The number you have chosen is {}'.format(secret) 
		if secret == 1:
			print '\n'
			print 'You now have a magic pair of boots! Hooray!'
			print '\n'
		if secret == 2:
			print '\n'
			print 'You now have a pet flying squirrel.'
			print 'Ride him like the wind!'
			print '\n'
		if secret == 3:
			print '\n'
			print 'You got nothing.'
			print 'Why did you make such a dumb decision?'
			print '\n'
		
	
	else:
		print 'That is not an option.'
		print '\n'
		return 0
		

def do_dungeons():
	print '\n'
	print 'You are in a dark and scary dungeon! Creeepy!!'
	print '\n'

def do_the_single_life():
	print '\n'
	print 'You are probably a lonely virgin. Good luck with that!'
	print '\n'
	
## list gamestuff var and ask them to choose
gamestuff = ['dragons','dungeons','mazes','the single life','secret item']	


while True:
	print 'What shall we do?'
	for item in gamestuff:
		print '* {}'.format(item)

## choose gamestuff, call a function or else not an answer (or exit to quit)	
	choice = raw_input('>>>')
	if choice.lower() in ['exit','quit']:
		print 'You have chosen to quit.'
		break;
	elif choice == 'dragons':
		do_dragons()
	elif choice == 'mazes':
		do_mazes()
	elif choice == 'secret item':
		do_secret()
	elif choice == 'dungeons':
		do_dungeons()
	elif choice == 'the single life':
		do_the_single_life()
	elif choice not in gamestuff:
		print 'come on now. That is not a choice.'
	else:
		print 'you chose "{}"'.format(choice)
		
	
			
	
	