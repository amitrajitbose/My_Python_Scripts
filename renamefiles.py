import os
import time
def rename_files():
    savedpath=(os.getcwd())
    #get all the file names from a folder
    filelist=os.listdir(r"C:\Users\HP\Desktop\Test") #here r indicates RAWPACK, You need to put your system path here
    #print(filelist)
    os.chdir(r"C:\Users\HP\Desktop\Test")
    #rename files
    for x in filelist:
        print("OLD NAME:  ",x)
        os.rename(x,x.lstrip("0123456789")) #removes numbers from the beginning
        print("NEW NAME:  ",x.lstrip("0123456789"))
        print("")
        #os.rename(x,x.rstrip(".txt12"))
        #os.rename(x,x+str(count))
    os.chdir(savedpath)    #to return back to the original folder dir

print("RENAMER IS LOADING....")
time.sleep(2)
rename_files()

print("Author: Amitrajit Bose")
input("Press ENTER To Exit Console")
