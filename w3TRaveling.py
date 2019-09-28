#-------------------------------------------------------------------------------
# Name:        Traveling Expences
# Purpose:
#
# Author:      Vlad
#
# Created:     26/02/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

FName=raw_input("Your name")
FName=str(FName)
EngineSize=input("Engine size in cc")
EngineSize=int(EngineSize)
Distance=input("Distance")
Distance=float(Distance)

if EngineSize<=1100:
    Cost=0.06*Distance
    print "Travel will cost you ",FName," ",Cost," Pounds"
elif EngineSize>1100 and EngineSize<=1500:
    Cost=0.07*Distance
    print "Travel will cost you ",FName," ",Cost," Pounds"
elif EngineSize>1500:
    Cost=0.08*Distance
    print "Travel will cost you ",FName," ",Cost," Pounds"
else:
    print "Input data is wrong"