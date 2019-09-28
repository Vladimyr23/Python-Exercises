#-------------------------------------------------------------------------------
# Name:        100CoinFlips
# Purpose:
#
# Author:      Vlad
#
# Created:     04/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

Heads=0
tails=0

for i in range(1,101):
    Coin = random.randrange(2)
    if Coin==0:
        Heads=Heads+1
    else:
        tails=tails+1

print "From 100 flips you've got ",Heads,"Heads and ",tails," Tails"

