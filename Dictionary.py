#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vlad
#
# Created:     29/03/2016
# Copyright:   (c) Vlad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------



keys = ['FirstName', 'LastName', 'SSID']
name1 = ['Michael', 'Kirk', '224567']
name2 = ['Linda', 'Matthew', '123456']

dictList = []
dictList.append(dict(zip(keys, name1)))
dictList.append(dict(zip(keys, name2)))

#print dictList
for item in dictList:
    print ' '.join([item[key] for key in keys])

