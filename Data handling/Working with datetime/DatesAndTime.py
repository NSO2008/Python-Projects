#It is necessary to import the datetime module when handling date and time
import datetime

currentTime = datetime.datetime.now()
currentDate = datetime.date.today()
#This will print the date
#print(currentDate)
#This the year
#print(currentDate.year)
#This the month
#print(currentDate.month)
#And this the day...
#print(currentDate.day)

#The "strftime()" function is a more common way for getting specific elements of date
#day = currentDate.strftime('%d')
#month = currentDate.strftime('%B')
#year = currentDate.strftime('%Y')

#This will print; "Today's date is the 13th of August, 2020."
#print("Today's date is the " + day + "th of " + month + ", " + year + ".")

print("Okay, what if I told you I could guess how many days till your birthday...")
userBirthday = input("When's your birthday? Write it here: ")
try:
    bday = datetime.datetime.strptime(userBirthday, '%d/%m/%Y').date()
except ValueError:
    print("Oh sorry, my bad... You are meant to put it in this format; dd/mm/yyyy.")
    userBirthday = input("When's your next birthday? Write it here: ")
    try:
        bday = datetime.datetime.strptime(userBirthday, '%d/%m/%Y').date()
    except ValueError:
        print("Invalid input... Input not processed...")


try:
    daysTillBday = bday - currentDate
    print("I think I got that... Ok, so there are " + str(daysTillBday.days) + " days till you birthday right?")
except:
    print("Uh oh... \nI couldn't really catch your birthday, no worries, there's always next time...")


print("Goodbye.")