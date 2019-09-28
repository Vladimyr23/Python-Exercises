#-------------------------------------------------------------------------------
# Name:        Translate +2
# Purpose: Python Challenge
#
# Author:      Vlad
#
# Created:     30/11/2015
# Copyright:   (c) Vlad 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

m = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
"""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

t = string.maketrans(m, m[13:] - m[:13])
print m.translate(t)