sortedWords = []
print("Welcome to the alphabetical sorter...")
questionOne = input("How many words do you wish to sort?: ")
questionOne = int(questionOne)
for words in range(questionOne):
    word = input("Please enter a word: ")
    sortedWords.append(word)

sortedWords.sort()

for sorting in sortedWords:
    print(sorting)