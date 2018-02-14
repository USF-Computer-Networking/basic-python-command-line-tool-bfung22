import argparse
import random

## Utilizes argparse to perform simple tasks.
## Use the ' -h' flag for help.
## @Benny Fung

def func():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-r1', '--random1', help = 'Adds inputted number by a random number from 1 - 10')
	group.add_argument('-r2', '--random2', help = 'Adds inputted number by a random number from 11 - 50')
	group.add_argument('-r3', '--random3', help = 'Adds inputted number by a random number from 51 - 100')
	group.add_argument('-r4', '--random4', help = 'Guess a number from 1 - 10000')
	group.add_argument('-m', '--morning', help = 'Print good morning', nargs = '?')
	group.add_argument('-a', '--afternoon', help = 'Print good afternoon', nargs = '?')
	group.add_argument('-n', '--night', help = 'Print good night', nargs = '?')
	group.add_argument('-f', '--file', help = 'Print all lines of input file', nargs = '?')

	return parser.parse_args()

def run(arg):
	if(arg.random1):
		try:
			val = int(arg.random1)
			print("Inputted number:", arg.random1) 
			num = random.randint(1,10)
			print("Random number:", num)
			print("Result:", int(arg.random1) + num)
		except ValueError:
			print("Input not a valid int.")
			return

	elif(arg.random2):
		try:
			val = int(arg.random2)
			print("Inputted number:", arg.random2) 
			num = random.randint(11,50)
			print("Random number:", num)
			print("Result:", int(arg.random2) + num)
		except ValueError:
			print("Input not a valid int.")
			return

	elif(arg.random3):
		try:
			val = int(arg.random3)
			print("Inputted number:", arg.random3) 
			num = random.randint(51,100)
			print("Random number:", num)
			print("Result:", int(arg.random3) + num)
		except ValueError:
			print("Input not a valid int.")
			return

	elif(arg.random4):
		try:
			val = int(arg.random4)
			num = random.randint(1,10000)
			print("Random number:",num)
			print("Your number:", arg.random4)
			if(val == num):
				print("You guessed correctly!")
			else:
				print("You guessed incorrectly")
		except ValueError:
			print("Input not a valid int.")
			return

	elif(arg.morning):
		print("Good morning, " + arg.morning + "!")

	elif(arg.afternoon):
		print("Good afternoon, " + arg.afternoon + "!")

	elif(arg.night):
		print("Good night, " + arg.night + "!")

	elif(arg.file):
		try:
			file = open(arg.file, 'r+')
			for lines in file:
				print(lines)
		except IOError:
			print("Cannot read file")
			return
	return

if __name__ == '__main__':
	arg = func()
	run(arg)