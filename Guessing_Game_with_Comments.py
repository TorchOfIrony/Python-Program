#Imports the random class from the Python directory.
import random

#This function, GuessingGame(), asks the user to enter a number between 1 and 10 in an attempt to guess that number.
def GuessingGame():

	#List of variables commonly used
	guesses_made = 0

	name = raw_input('Good day to you! Who are you?\n')

	number = random.randint(1, 10)
	
	willToContinue = True
	
	print 'Well, {0}, Shall we play a little game for fame? I am thinking of a number between 1 and 10.'.format(name)
	#First while statement checks to see if the user is willing to continue playing the game. For the first round
	#it is assumed the user wishes to play, but is then asked after three guesses.
	while willToContinue == True:
	
		#Second while statement asks the user to guess a number and, depending on what that number is, determines
		#whether to continue asking for a number (up to three total guesses) or to break if the user guessed the
		#correct number.
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
#End GuessingGame() function.