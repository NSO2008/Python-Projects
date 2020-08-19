#Lists are equivalent to arrays
#Lists are used to contain much data
#Examples
names = ["Samuel", "Bryan", "Julie", "Chima"]
ages = [12, 5, 45, 47]
lastNames = []
height = []
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])
names[-1] = "Ifechukwu"
print("The last name is now " + names[-1])
names.append("Chima")
print("Yay! The last name in the list is now " + names[-1])
print("And the 2nd name from behind is now " + names[-2])
names.remove(names[-2])
del names[-1]
print("And now both names are removed! The last name is now " + names[-1])
print("And the name that is second from behind is now " + names[-2])
print("Now let's see the names of the people in the list.")
for name in names:
    print(name)
