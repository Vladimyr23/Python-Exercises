#-------------------------------------------------------------------------------
# Name:        AssesmPasssword
# Purpose:
#
# Author:      Vladimir Yesipov
#
# Created:     25/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Import random number generator library
import random
import math

#lists of users and Passswords Creation
users=[]
passwords=[]
selection=0

#Sign-in function
def SignIn(re_try):
    Name=''
    Password=''

    while (Name not in users) and (Password not in passwords) and re_try>0:
        re_try=re_try-1
        Name=str(raw_input("Please enter your name \n M-back to the main menu")).capitalize()
    #Main menu return
        if Name=='M':
            login=False
            break
    #Password check
        Password=str(raw_input("Please enter your password"))
    #Name and Password check
        if Name in users:
            uon=users.index(Name)
            if Password==passwords[uon]:
                login=True
                print "Welcome ",Name
            else:
                print"Incorrect password"
                login=False
        else:
            print"This name is not in our base"
            login=False
    return login

#First visit SignUp function
def SignUp():
    Name=''
    Password=''
    Password1=''

    for attempt in range (1,4):
        Name=raw_input("Please enter your name \n M-back to the main menu")
        Name=(str(Name)).capitalize()
    #Main menu return
        if Name=='M':
            break
    #Password input
        Password=raw_input("Please enter your password")
        Password=str(Password)
        Password1=raw_input("Please approve your password")
        Password1=str(Password1)
    #Adding only when passwords match
        if Password==Password1:
    #Only unique name can be added into the users list
            if Name in users:
                    print "This name is already in use. \n Please choose different name."
            else:
                    users.append(Name)
                    passwords.append(Password)
                    print "Your name and password now in our database"
                    break
        else:
                print"Your password inputs don't match"

#Main program code
while selection!=3:

#Main menu
    print \
    """
    Please make your selection
    1. Sign-up
    2. Sign-in
    3. Exit
    """
#Main menu selection input
    selection=int(raw_input())

#SignUp function call
    if selection == 1:
        SignUp()

#SignIn function call
    elif selection == 2:
        sign_in=SignIn(3)

#SignIn result
        if sign_in==True:
            LuckNum=(random.randrange(10,100))/float(10.0)
            print "Your lucky decimal number for today is ",LuckNum
        else:
            print "Try again another time"

#Main menu input validation
    elif selection!=1 and selection!=2 and selection!=3:
        print "Type 1, 2 or 3"

#Program final message
print "Good Buy. See you next time."

