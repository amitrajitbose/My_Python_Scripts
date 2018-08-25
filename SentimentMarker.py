# Author: Amitrajit Bose
# https://amitrajitbose.github.io

import re
import xlsxwriter
from textblob import TextBlob
import pandas as pd
import os

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ /\ / \S +)", " ", tweet).split())

os.chdir(r"C:\Users\..YOUR PROJECT FOLDER")
file='myfile.xlsx' #this is the excel sheet that contains the details
x1=pd.ExcelFile(file)
df1=x1.parse('Sheet1')
mat=(df1.as_matrix())
rows=mat.shape[0]

positivecounter=0
neutralcounter=0
negativecounter=0

for i in range(rows):
	s = str(mat[i][3])
	#cleaning the comment
	s = clean_tweet(s)
	blob = TextBlob(s)
	#because I am storing the feedback in tenth column of the new excel sheet
	if((blob.sentiment.polarity)>0.5):
		mat[i][10]='Positive'
		positivecounter+=1
	elif((blob.sentiment.polarity)<0):
		mat[i][10]='Negative'
		negativecounter+=1
	else:
		mat[i][10]='Neutral'
		neutralcounter+=1

df1=pd.DataFrame(mat,columns=['S No.','Hospital Name','Name of the person','Comment','Total Reviews','Individual likes','Star Rating by individuals','Views','Overall rating','Recommended by members (in %)','Polarity'])
writer = pd.ExcelWriter('Output.xlsx', engine='xlsxwriter')
df1.to_excel(writer, 'Sheet1')
writer.save()

print("****************************\nPROCESS COMPLETE\nEXCEL FILE GENERATED\n\nCOMMENT STATISTICS")
print("----------------------------------")
print("POSITIVE: {0:.3f} %\tCOUNT: {1}".format((positivecounter*100)/rows,positivecounter))
print("NEUTRAL: {0:.3f} %\tCOUNT: {1}".format((neutralcounter*100)/rows,neutralcounter))
print("NEGATIVE: {0:.3f} %\tCOUNT: {1}".format((negativecounter*100)/rows,negativecounter))
print("---Author: Amitrajit Bose---")


'''
DEPENDENCIES:
xlrd==1.1.0
XlsxWriter==1.0.5
textblob==0.15.1
pandas==0.22.0
'''