#-------------------------------------------------------------------------------
# Name:        Actress Casting
# Purpose:  Iteration, Objects
#
# Author:      Vladimir Yesipov
#
# Created:     26/02/2016
# Copyright:   (c) Vladimir 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#NextActress=raw_input("Do you want to work next actress data(Yes/No)")
#NextActress
#NextActress=str.upper(NextActress)


#if NextActress=='YES':
HairColor=raw_input("What is the hair colour she has?")
HairColor=str(HairColor)
HairColor=str.lower(HairColor)
Age=input("Her Age.")
Age=int(Age)
HairTexture=raw_input("Her hair texture (curly/straight)")
HairTexture=str(HairTexture)
HairTexture=str.lower(HairTexture)
Height=input("Her height")
Height=float(Height)
if (HairColor=='brown' or HairColor=='red') and Age==11 and HairTexture=='curly' and Height<1.5:
        print 'She passes on to the next selection stage'
else:
        print "Sorry she didn't pass"
