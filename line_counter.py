#!/usr/bin/env python
#
# Go through a directory (and sub-directories) and count the number of lines in each file.
#
# Usage:
#
# python count_lines.py --path /www/sites/ --count java,xml
# python count_lines.py --path /www/sites/ --count py
#

import os
import sys

def shouldAllow( name, allowed ):
	for ext in allowed : 
		if name.endswith( "." + ext ) :
			return True
	return False

if __name__ == "__main__" :	
	lines = 0
	path = "."
	
	if "--path" in sys.argv:
		path = sys.argv[sys.argv.index('--path') + 1]
	
	allowed = []
	if "--count" in sys.argv:
		allowed = sys.argv[sys.argv.index('--count') + 1].split(",")

	print "Using path: ", path
	
	for root, dirs, files in os.walk(path):
		print "Inside " + root
		for name in files:
			if shouldAllow( name, allowed ):
				pathToFile = os.path.join(root, name )
				foo = open( pathToFile, "r" ).readlines()
				lines += len(foo)
				print len(foo), " lines in ", "\t"+name
	
	print "Total lines: ", lines
