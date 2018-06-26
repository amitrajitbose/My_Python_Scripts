
# coding: utf-8
# @Author: Amitrajit Bose
# In[104]:
'''
Suppose you have a folder which contains files of two categories but are of random names.
Assuming that there are more than 100, 1000, 10000 or more files and they cannot be copied separately one by one due to time limitation.
You have an excel sheet where in all the files are listed with their names (and extension) and their corresponding labels are assigned
in the next corresponding cell, in next column.
We need to create two folder (or more if needed) and one by one copy a file and paste it to that folder.
This script does the job in just one click and seconds of time.
'''

#This is a Python script to separate files based on the data given on an excel sheet.
#Here we have separated it to two classes - classA,classB
#Author: Amitrajit Bose


# In[105]:


import pandas as pd
import shutil
import os
os.chdir(r"C:\Users\PC\Documents") #put your path here where all the files are present
file='classification.xlsx' #this is the excel sheet that contains the details
x1=pd.ExcelFile(file)
df1=x1.parse('Sheet1')
mat=(df1.as_matrix())
rows=mat.shape[0]
#print(mat.shape) #this is a rows x column matrix or numpy array extracted from excel sheet
files=[]
labels=[]
for i in range(rows):
    files.append(str(mat[i][0]))
    labels.append(str(mat[i][1]))
#the list images contain all the file names/directories i.e the first column of the sheet
#the list labels contain their corresponding label i.e the second column of the sheet


# In[106]:


savedpath=os.getcwd()
memofolder=r"C:\Users\PC\Documents\myfolder"
for i in range(rows):
    item=memofolder+'\\'+files[i].strip(' ')
    filename=files[i].split('/')[-1]
    item=item.replace("/","\\")
    
    ifclassA="C:\\Users\\PC\\Documents\\classA\\"+filename
    ifclassB="C:\\Users\\PC\\Documents\\classB\\"+filename
    if(labels[i]=="Class A"):
        #place in classA folder
        shutil.copy(item,ifclassA)
    elif(labels[i]=="Class B"):
        #place in classB folder
        shutil.copy(item,ifclassB)

