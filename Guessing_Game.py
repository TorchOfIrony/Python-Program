import random

def GuessingGame():

	guesses_made = 0

	name = raw_input('Hello! What is your name?\n')

	number = random.randint(1, 20)
	
	willToContinue = True
	choiceOfContinue
	
	print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)
	while willToContinue == True:
	
		while guesses_made < 6:

			guess = int(raw_input('Take a guess: '))

			guesses_made += 1

			if guess < number:
				print 'Your guess is too low.'

			if guess > number:
				print 'Your guess is too high.'

			if guess == number:
				break

		if guess == number:
		
			print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)
			
		else:
		
			print 'Nope. The number I was thinking of was {0}'.format(number)
			
		choiceOfContinue = raw_input('So, {0}... want to play another round?(Type "yes", "y", or "no", "n")\n'.format(name))
		
		if choiceOfContinue == 'yes' *or* choiceOfContinue == 'y':
		
			willToContinue = True
			
		elif choiceOfContinue == 'no' *or* choiceOfContinue == 'n':
		
			willToContinue = False
			
		else
		
			willToContinue = False
		
