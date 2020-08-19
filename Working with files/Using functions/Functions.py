filepath = "Functions_data.txt"
READ = "r"
WRITE = "w"
APPEND = "a"
listOfWords = []
def printWords():
    print(names)
    return


def main():
    numOfNames = input("Enter the number of words/text/phrases/sentences you wish to remember: ")
    for questions in range(int(numOfNames)):
        words = input("Enter some text: ")
        with open(filepath, mode=APPEND) as myFile:
            myFile.write(words + "\n")


    yesNo = input("Do you wish to see all past entries?(Y/N): ")
    yesNo = yesNo.lower()


    if yesNo == "y":
        with open(filepath, mode=READ) as myFile:
            names = myFile.read()
            printWords()
    else:
        print("Have a nice day.")


options = input("Do you wish to enter new txt or to remember of view past entries?(A/B): ")
options = options.lower()
if options == "a":
    main()
else:
    print("Here are your past entries.")
    with open(filepath, mode=READ) as myFile:
            names = myFile.read()
            printWords()
    print("Have a nice day.")
