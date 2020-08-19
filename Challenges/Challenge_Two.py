L = input("Please enter your loan amount: ")
try:
    L = float(L)
except ValueError:
    print("Pls enter a valid number")
    try:
        L = input("Please enter your loan amount: ")
        L = float(L)
    except ValueError:
        print("Error found... Code cannot be executed.")

#Ask the user for their interest rate
i = input("Pls enter your interest rate without the percentage sign: ") 
try:
    i = float(i)
except ValueError:
    print("Pls enter a valid number")
    try:
        i = input("Pls enter your interest rate without the percentage sign: ")
        i = float(i)
    except ValueError:
        print("Error found... Code cannot be executed.")

#Manually convert interest rate to a floating number
try:
    i = i/100
    i = float(i)
except:
    print("Something went wrong... Code has failed to execute.")

n = input("Please enter your number of payments: ")
try:
    n = float(n)
except ValueError:
    print("Pls enter a valid number")
    try:
        n = input("Please enter your number of payments: ")
        n = float(n)
    except ValueError:
        print("Error found... Code cannot be executed.")


try:
    M = (L*(i*(1+i)*n)) / ((1+i)*(n-1)) 
except:
    print("An error occured... Vital code has failed to execute...")


try:
    print("Your monthly payment is: " + str(M) + "...\nThe code has been successfully executed.")
except TypeError:
    print("Uh oh... There is a problem somewhere... Your input has not been successfully processed...")
except NameError:
    print("Uh oh... There is a problem somewhere... Your input has not been successfully processed...")
except ValueError:
    print("Uh oh... There is a problem somewhere... Your input has not been successfully processed...")
except SyntaxError:
    print("Uh oh... There is a problem somewhere... Your input has not been successfully processed...")
except:
    print("Uh oh... There is a problem somewhere... Your input has not been successfully processed...")
finally:
    print("Goodbye...")

