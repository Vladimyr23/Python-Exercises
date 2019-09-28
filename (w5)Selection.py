#-------------------------------------------------------------------------------
# Name:        W5Selection
# Purpose:
#
# Author:      Vlad
#
# Created:     17/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#data input
Adults=input("How many adults in the group?")
Children=input("How many children in the group?")
Adults=int(Adults)
Children=int(Children)
Day=raw_input("Day of the week")
Day=str.capitalize(Day)

#Calculation
if Day=="Saturday" or Day=="Sunday":
    Cost=Adults*10+Children*5
else:
    Cost=(Adults+Children)*5

#Result output
print"Tickets cost for this group is ", Cost