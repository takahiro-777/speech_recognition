# -*- coding: utf-8 -*-
# http://aidiary.hatenablog.com/entry/20120805/1343825329

#import modules
import struct
import sys
import numpy as np

# print_mfcc.py

if len(sys.argv) != 3:
    print "usage: python print_mfcc.py [mfcc_file] [m]"
    sys.exit()

mfccfile = sys.argv[1]
m = int(sys.argv[2])

mfcc = []
f = open(mfccfile, "rb")
while True:
    b = f.read(4)
    if b == "": break;
    val = struct.unpack("f", b)[0]
    mfcc.append(val)
f.close()

mfcc = np.array(mfcc)
numframe = len(mfcc) / m

if numframe * m != len(mfcc):
    print "ERROR: #mfcc:%d #frame:%d m:%d" % (len(mfcc), numframe, m)
    sys.exit(1)

mfcc = mfcc.reshape(numframe, m)
for i in range(len(mfcc)):
    print "\t".join("%.2f" % x for x in mfcc[i,])
