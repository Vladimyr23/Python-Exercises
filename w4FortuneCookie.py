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

#User=input("Please type \n 1 for Rock \n 2 for Paper \n 3 for Scissors")
#User=int(User)
Comp=random.randrange(5)
if Comp==0:
    print "You must try, or hate yourself for not trying."
elif Comp==1:
    print "A friend asks only for your time not your money."
elif Comp==2:
    print "Hard work pays off in the future, laziness pays off now."
elif Comp==3:
    print "Change can hurt, but it leads a path to something better."
elif Comp==4:
    print "If you have something good in your life, don't let it go!"
