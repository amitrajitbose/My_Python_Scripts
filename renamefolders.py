import os
import time
import xlsxwriter
import pandas as pd
def rename_files():
    savedpath=(os.getcwd())
    #get all the file names from a folder
    filelist=os.listdir(r"C:\Users\...\Desktop\Project") #here r indicates RAWPACK, You need to put your folder path here
    #print(filelist)
    os.chdir(r"C:\Users\...\Desktop")
    file='renameInstructions.xlsx' #this is the excel sheet that contains the details
    x1=pd.ExcelFile(file)
    df1=x1.parse('Sheet1')
    mat=(df1.as_matrix())
    rows=mat.shape[0] #total number of folder according to excel sheet
    basedir = 'C:/Users/.../Desktop/Project' #change this as per requirement
    if(len(filelist)==rows):
        for i in range(rows):
            print("OLD NAME: ",filelist[i])
            os.rename(os.path.join(basedir, filelist[i]), os.path.join(basedir, mat[i][0])) #essentially for folder renaming
            print("NEW NAME: ",mat[i][0],"\n")
    else:
    	print("ERROR : Folder count and row count on excel sheet do not match\n")

    
print("RENAMER IS LOADING....\n")
time.sleep(2)
rename_files()

print("Developed by Amitrajit Bose")


