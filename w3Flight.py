#-------------------------------------------------------------------------------
# Name:        Flight
# Purpose:
#
# Author:      Vlad
#
# Created:     19/02/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def reportstatus(scheduled,ETA):
    status=''
    if scheduled==ETA:
        status='On time'
    elif scheduled>ETA:
        status='Early'
    else:
        status='Delayed'
    return status

scheduled=12.0
ETA=raw_input("please enter an actual arrival time")
ETA=float(ETA)
status=reportstatus(scheduled,ETA)
print status


