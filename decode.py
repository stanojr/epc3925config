#!/usr/bin/python

import sys

xor=ord('#')^ord('2')

#print xor
#print hex(xor)

with open ("filename.gwc", "r") as myfile:
    data=myfile.read()


firstline = data.splitlines(True)[0]
encodedlines = ''.join(data.splitlines(True)[1:])

sys.stdout.write(firstline)

for i, c in enumerate (encodedlines):
    sys.stdout.write(chr(xor^ord(c)))

