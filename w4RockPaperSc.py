#-------------------------------------------------------------------------------
# Name:        Rock,Paper,Scissors
# Purpose:
#
# Author:      Vlad
#
# Created:     04/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

User=input("Please type \n 1 for Rock \n 2 for Paper \n 3 for Scissors")
User=int(User)
Comp=random.randrange(3)
if Comp==(User-1):
    print "You and Computer made the same selection"
elif Comp==0 and User==2:
    print "You won. Computer choice is Rock."
elif Comp==0 and User==3:
    print "You Lost. Computer choice is Rock."
elif Comp==1 and User==1:
    print "You Lost. Computer choice is Paper."
elif Comp==1 and User==3:
    print "You Won. Computer choice is Paper."
elif Comp==2 and User==1:
    print "You Won. Computer choice is Scissors."
elif Comp==2 and User==2:
    print "You Lost. Computer choice is Scissors."
else:
    print "Your choice is inappropriate."