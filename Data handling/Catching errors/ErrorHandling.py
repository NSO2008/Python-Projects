import sys
first = input("Enter your first number: ")

second = input("Enter your second number: ")

try:
    result = float(first) / float(second)
    print("Your answer is " + str(result))
except ZeroDivisionError:
    result = "Your answer is ∞"
    print(result)
    sys.exit()
except:
    error = sys.exc_info()[0]
    print("Something went wrong.")
    print("Please contact the support team and give them the following error:")
    print(error)
    sys.exit()
finally:
    print("Goodbye.")

print("Your division was performed perfectly")
