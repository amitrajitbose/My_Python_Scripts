#Division with Try & Except block
#import time
def divide(a,b):
	#divides a by b
	#normally the program would crash if b=0, but not in this case
	try:
		return (a/b)
	except ZeroDivisionError:
		print("You cannot divide a number by zero!")
		#time.sleep(2)
		exit()

x=(input("Enter Numerator: "))
y=(input("Enter Denominator: "))
try:
	x=int(x)
	y=int(y)
	print(divide(x,y))
except ValueError:
		print("You have to enter an integer!")
		exit()
#time.sleep(2)
