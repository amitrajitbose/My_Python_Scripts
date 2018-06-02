import webbrowser
import time
print("Current Time: "+time.ctime()) #shows the current time
n=int(input("How many breaks do you need? "))
for loop in range(n):
	'''
	just change this time as per your requirement, this is in seconds.
	Currently set at five seconds, to make the gap of thirty minutes put 30*60'''
    time.sleep(5)
    webbrowser.open_new("https://youtu.be/b_n3IJfW8Dg?t=6") #I kinda like this song, you can customize
