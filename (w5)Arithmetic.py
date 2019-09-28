#-------------------------------------------------------------------------------
# Name:        (W5)ArifmethicMultipl
# Purpose:
#
# Author:      Vlad
#
# Created:     11/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Pakets import
import random

Correct=0
Answer=1
#Main Loop
while Correct!=10 and Answer!=0:

#Difficulty Selection
    if Correct<4:
        first=random.randrange(10)+1
        second=random.randrange(10)+1
    elif Correct>3 and Correct<8:
        first=random.randrange(10)+1
        second=random.randrange(100)+1
    else:
        first=random.randrange(100)+1
        second=random.randrange(100)+1

#Answer input
    #print "Please, enter the result of multiplication \n", first," and ", second, "\n or 0 to exit"
    Answer=input("Please, enter the result of multiplication \n"+ str(first)+" and "+ str(second)+ "\n or 0 to exit")
    Result=first*second
    Answer=int(Answer)

#Answer validation
    if Answer==Result:
        Correct=Correct+1
        print "That's right. Well done."
        print "To finish exercise you have to answer 10 questsions in a raw. \n And your result is ", Correct, "Answers"
    else:
        Correct=0
        print "No, the correct answer is", Result

#final message
if Correct==10:
    print "Congratulations. \n You`ve answered 10 questions in a row correct. \n Well Done."
else:
    print "Bye. See you next time. \n Your result is ", Correct, " Answers"




