import random

def GuessingGame():

	guesses_made = 0

	name = raw_input('Good day to you! Who are you?\n')

	number = random.randint(1, 10)
	
	willToContinue = True
	
	print 'Well, {0}, Shall we play a little game for fame? I am thinking of a number between 1 and 10.'.format(name)
	while willToContinue == True:
	
		while guesses_made < 3:

			guess = int(raw_input('Come, now, take a guess: '))

			guesses_made += 1

			if guess < number:
				print 'Sorry, your guess is just too low.'

			if guess > number:
				print 'Sorry, your guess is just too high.'

			if guess == number:
				break

		if guess == number:
		
			print 'Good on you, {0}! You have guessed my number in {1} guesses!'.format(name, guesses_made)
			
		else:
		
			print 'Haha! The number I was thinking of was {0}!'.format(number)
			
		choiceOfContinue = raw_input('So, {0}... want to play another round?(Type "yes", "y", or "no", "n")\n'.format(name))
		
		if choiceOfContinue == 'yes' *or* choiceOfContinue == 'y':
		
			willToContinue = True
			
		elif choiceOfContinue == 'no' *or* choiceOfContinue == 'n':
		
			willToContinue = False
			
		else
		
			willToContinue = False
			
		if willToContinue == False
		
			print 'Well, take care,  {0}! Until next you run this program!'.format(name)
