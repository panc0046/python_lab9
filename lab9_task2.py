import os.path, csv
from os import path

# Take input from user for file name
print("Files: 1.Names_Boys 2.Names_Girls")
file_name = input("Enter file name define above")

# Check whether file is exist or not
if path.exists(file_name+".csv") == True:
    files = open(file_name+".csv","r")
    reader = csv.reader(files)
    mainList = []
    counter = 1
    for row in reader:
        if counter == 1:
            counter=0
            continue
        else:
            mainList.append(row)
    print(mainList)
else:
    print("File Does not exist. Please enter valid file name!")