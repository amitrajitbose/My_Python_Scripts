import webbrowser
import time

print ("Enter Timer In Seconds: ")
sec=int(input())
print ("Paste Your Link Here: ")
link=str(input())
if(len(link)==0):
    link="https://youtu.be/dT2owtxkU8k?t=26" #Shawn Mendes Song Youtube Link
time.sleep(sec)
webbrowser.open(link)
