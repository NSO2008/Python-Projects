#The syntax for opening a file is "myFile = open(fileName, accessMode)".
#It is best to store the parameters in a variable in order to access it easily.\
import csv
filepath = "data.csv"
READ = "r"
WRITE = "w"
APPEND = "a"
myFile = open(filepath, mode=WRITE)
print("File opened")
myFile.write("Julie, 45\n")
myFile.write("Chima, 47\n")
myFile.close()
print("File closed")
myFile = open(filepath, mode=READ)
print("File opened")
fileContent = myFile.read()
print(fileContent)
myFile.close()
print("File closed")
myFile = open(filepath, mode=APPEND)
print("File opened")
myFile.write("Samuel, 12\n")
myFile.write("Bryan, 5\n")
myFile.close()
print("File closed")
myFile = open(filepath, mode=READ)
print("File opened")
fileContent = myFile.read()
print(fileContent)
myFile.close()
print("File closed")
with open(filepath, mode=READ) as myFile:
    print("File opened")
    fileContent = csv.reader(myFile)
 
    for filePhrases in fileContent:
        print(', '.join(filePhrases))

print("File closed")
print("Program terminated.")
