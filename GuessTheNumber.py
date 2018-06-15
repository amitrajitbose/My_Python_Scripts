#Guess The Number Game
#Automate The Boring Stuff With Python
#Author: Al Swegart

import random
name=input("Hi! What's your name? ")
print("Well, "+name+", I am guessing a number between 1 and 20.\nCan you guess?\n")
secretNo=random.randint(1,20)
for guess in range(7):
	guessNo=int(input("Take a guess! "))
	if(guessNo>secretNo):
		print("You've crossed it. Try again!")
	elif(guessNo<secretNo):
		print("Keep going!")
	else:
		break
if(guessNo==secretNo):
	print("Good Job "+name)
else:
	print("Oops. Too many attempts\nThe number is "+str(secretNo))
