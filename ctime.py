#!/usr/bin/python
# this is a program to check the current time
#loads time module
import time
print "press 1 to check current time:"
print "press 2:"
#to take input from user
ch=raw_input("press 1 or 2:")
if ch=='1':
	print time.ctime()
else:
	print "you must have entered 1"

