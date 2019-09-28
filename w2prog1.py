#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vlad
#
# Created:     15/02/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

length=raw_input("length of the room in meters")
width=raw_input("width of the room in meters")
CarpetMeterPrice=raw_input("Carpet price 1 sqr meter")
length=float(length)
width=float(width)
CarpetMeterPrice=float(CarpetMeterPrice)

square=length*width
CarpetPrice=CarpetMeterPrice*square
print "Carpet Price for this room is ",CarpetPrice

length=raw_input("length of the garden in meters")
width=raw_input("width of the garden in meters")

length=float(length)
width=float(width)

fence=(length+width)*2-width
print "Fencing length", fence
