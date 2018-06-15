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

x=int(input("Enter Numerator: "))
y=int(input("Enter Denominator: "))
print(divide(x,y))
#time.sleep(2)
