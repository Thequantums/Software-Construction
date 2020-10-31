#!/usr/local/cs/bin/python3

"""
Output lines selected randomly from a file

Copyright 2005, 2007 Paul Eggert.
Copyright 2010 Darrell Benjamin Carbajal.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Please see <http://www.gnu.org/licenses/> for a copy of the license.

$Id: randline.py,v 1.4 2010/04/05 20:04:43 eggert Exp $
"""

import random, sys
from optparse import OptionParser

class randline:
    def __init__(self,args,irange, hcount, repeat):       	
        if irange=='100-10' and (len(args)==0 or args[0]=='-'):
                self.input_elem = sys.stdin.readlines();
        elif irange != '100-10' :
                for i in range(len(irange)):
                    if irange[i] == '-':
                       posi = i
                lo = int(irange[0:posi])
                hi = int(irange[posi+1:])
                for t in range(lo,hi):
                        if t == lo:
                           self.input_elem = (t,)
                        else:
                           self.input_elem = self.input_elem + (t,)
                self.input_elem = self.input_elem + (hi,) 
        else:
                f = open(args[0], 'r')
                self.input_elem = f.readlines()
                f.close()

        if hcount > len(self.input_elem) and not repeat:
           self.hcount = len(self.input_elem)
        else:
           self.hcount = hcount
	
        self.repeat = repeat
        self.args = args
        self.irange = irange
	
    def chooseline(self):
        if self.repeat == False:
             for i in range(self.hcount):
                        n = 0;
                        ran_num = random.choice(self.input_elem)
                        if i:
                                flag = 0
                                while flag == 0:
                                        flag = 1
                                        n = 0
                                        while n < len(exist):
                                           if ran_num == exist[n]:
                                             flag = 0
                                           n = n + 1
                                        if flag == 0:
                                           ran_num = random.choice(self.input_elem)
                                exist = exist + (ran_num,)
                        else: 
                                exist = (ran_num,)	
                        sys.stdout.write(str(ran_num) + '\n')
        elif self.hcount != sys.maxsize and self.repeat==1:
             for i in range(self.hcount):
                 sys.stdout.write(str(random.choice(self.input_elem)) + '\n')
        else:
             i = 1
             while i:
               sys.stdout.write(str(random.choice(self.input_elem)) + '\n') 

def main():
    version_msg = "%prog 1.0"
    usage_msg = """%prog [OPTION]... FILE
	or: %prog -i LO-HI [OPTION]...
		

Output randomly selected lines from FILE."""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-n", "--numlines",
                      action="store", dest="hcount", default=sys.maxsize,
                      help="output NUMLINES lines (default 1)")
    parser.add_option("-i", "--input-range", action="store", dest="irange",
		     default='100-10',help="output permutation of numbers in range")
    parser.add_option("-r", "--repeat", action="store_true", dest="repeat",
		     default=False,help="output non-permutation")
    options, args = parser.parse_args(sys.argv[1:])
    try:
        hcount = int(options.hcount)
    except:
        parser.error("invalid NUMLINES: {0}".
                     format(options.hcount))
    try:
        for i in range(len(options.irange)):
           if options.irange[i] =='-':
              posi = i
        s1 = options.irange[0:posi]
        lo = int(s1)
        s2 = options.irange[posi+1:]
        hi = int(s2)
        irange = options.irange
    except:
        parser.error("invalid range: {0}".format(options.irange))

    try:
        repeat = bool(options.repeat)
    except:
        parser.error("invalid option -- {0}".format(options.repeat))

    if hcount < 0:
        parser.error("negative count: {0}".
                     format(hcount))
    if len(args) > 1:
        parser.error("wrong number of operands")

    try:
        generator = randline(args,irange,hcount,repeat)
        generator.chooseline()
    except IOError as error:
        errno = error.errno
        strerror = error.strerror
        parser.error("I/O error({0}): {1}".
                     format(errno, strerror))

if __name__ == "__main__":
    main()


