#-------------------------------------------------------------------------------
# Name:        W5Iteration
# Purpose:
#
# Author:      Vlad
#
# Created:     17/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Start Day
Day=raw_input("Day of the week")
Day=str(Day)
Day=str.capitalize(Day)
EndDay=0
Total=0

#Iteration start
while EndDay!=1:

#data input
    Adults=input("How many adults in the group?")
    Children=input("How many children in the group?")
    Adults=int(Adults)
    Children=int(Children)


#Calculation
    if Day=="Saturday" or Day=="Sunday":
        Cost=Adults*10+Children*5
    else:
        Cost=(Adults+Children)*5
#Daily total
    Total=Total+Cost

#Result output
    print"Tickets cost for this group is ", Cost
    EndDay=input("Enter 1 to finish the day \n 0 to take next customer")
    EndDay=int(EndDay)
    if EndDay==1:
        break

#Daily total output
print Day + " total income is ", Total