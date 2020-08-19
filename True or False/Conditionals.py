#Conditional statements check if a statement is true or false
#Then they execute a command according to whether the statement is true or false
#The capital letter in true or false is important in python
# == is equal to (different from variable assignment)
# != is not equal to
# < is less than
# > is greater than
# <= is less than or equal to
# >= is greater than or equal to

total = 0
selectedProduct = input("What do you wish to buy? (Type \"Help\" to see list of items): ")
selectedProduct = selectedProduct.lower()
if selectedProduct == "fish":
    total = total+20
    print("That is a price of $" + str(total) + "...")
    yesNo = input("Would you like express shipping?(Y/N): ")
    yesNo = yesNo.upper()
    if yesNo == "Y":
        total = total+10
        print("That would be a total of $" + str(total) + "...")
    else:
        print("That would be a total of $" + str(total) + "...")
elif selectedProduct == "help":
    print("Help \nAt this company... We are proud sellers of fish... \nSo, we only offer fish... But at the best quality possible.")
    selectedProduct = input("So do you wish to purchase fish? (Y/N): ")
    selectedProduct = selectedProduct.lower()
    if selectedProduct == "y":
        total = total+20
        print("That is a price of $" + str(total) + "...")
        yesNo = input("Would you like express shipping?(Y/N): ")
        yesNo = yesNo.upper()
        if yesNo == "Y":
            total = total+10
            print("That would be a total of $" + str(total) + "...")
        elif yesNo == "N":
            print("That would be a total of $" + str(total) + "...")
    else:
        print("Okay...")
else:
    print("We do not offer that here, pls type help below for a list of products.")
    selectedProduct = input("What do you have in mind to purchase?: ")
    selectedProduct = selectedProduct.lower()
    if selectedProduct == "help":
        print("We offer only fish")
        selectedProduct = input("So do you wish to purchase fish? (Y/N): ")
        selectedProduct = selectedProduct.lower()
        if selectedProduct == "y":
            total = total+20
            print("That is a price of $" + str(total) + "...")
            yesNo = input("Would you like express shipping?(Y/N): ")
            yesNo = yesNo.upper()
            if yesNo == "Y":
                total = total+10
                print("That would be a total of $" + str(total) + "...")
            else:
                print("That would be a total of $" + str(total) + "...")
    elif selectedProduct == "fish":
        total = total+20
        print("That is a price of $" + str(total) + "...")
        yesNo = input("Would you like express shipping?(Y/N): ")
        yesNo = yesNo.upper()
        if yesNo == "Y":
            total = total+10
            print("That would be a total of $" + str(total) + "...")
        else:
            print("That would be a total of $" + str(total) + "...")
    else:
        print("I still do not understand...")
print("Have a nice day.")