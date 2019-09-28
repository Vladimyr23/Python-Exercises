#-------------------------------------------------------------------------------
# Name:        Inurance
# Purpose:
#
# Author:      Vlad
#
# Created:     26/02/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Type=raw_input("S-sport, N-normal")
Type=str(Type)
Type=str.upper(Type)
Age=input("Your age is")
Age=int(Age)
Fuel=input("Please, select the type of the fuel your car uses\n 1.Diesel \n 2. Unleaded Petrol")
if Type=="S":
    Insurance=int(300)+100
    if Age<25:
        Insurance=Insurance+50
        if Fuel==2:
            Insurance=float(Insurance)+Insurance*0.1
        elif Fuel!=1 or Fuel!=2:
            Insurance=str("Fuel type input is wrong")
    elif Age>90 or Age<18:
        Insurance=str("Age input is wrong")
elif Type=="N":
    Insurance=int(300)
    if Age<25:
        Insurance=Insurance+50
        if Fuel==2:
            Insurance=float(Insurance)+Insurance*0.1
        elif Fuel!=1 or Fuel!=2:
            Insurance=str("Fuel type input is wrong")
    elif Age>90 or Age<0:
        Insurance=str("Age input is wrong")
else:
    Insurance=str("Car type input is wrong")
if type(Insurance)==str:
    print Insurance
else:
    print "The estimate for your insurance is ",Insurance," Pounds"
