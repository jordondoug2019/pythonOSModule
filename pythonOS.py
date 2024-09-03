#Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input).
 #The script should display the total number of items (both files and directories) present in the specified directory.
 #Bonus Modify your script to count the number of files and directories separately. Hint: use the os module

 #Counts number of files/directories in a specific directoy 
 #takes said directory as input ("Enter the name of the directory")
 #display number of items in directory 

import os

directoryInput=input(f"Please enter the Directory you would like to check: " )

directoryList= os.listdir(directoryInput)
print(directoryList)
print(f"There are {len(directoryInput)} items in {directoryInput}")