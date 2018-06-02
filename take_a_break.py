import webbrowser
import time
print("Current Time: "+time.ctime()) #shows the current time
n=int(input("How many breaks do you need? "))
for loop in range(n):
    time.sleep(5)
    webbrowser.open_new("https://youtu.be/b_n3IJfW8Dg?t=6")
