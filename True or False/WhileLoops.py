#While loops are commonly used when number of loops is not specified
answer = input("I think of a number... can you guess it? \nWrite your answer right here: ")

while answer != '42':
    answer = input("Not quite there yet... Another guess?: ")
    
print("Congrats you got it!")

counter = 0
while counter < 4:
    print(counter)
    counter += 1