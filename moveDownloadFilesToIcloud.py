#!/usr/local/bin/python3.4
#
#Move files downloaded in the last hour "Recently" to specified location
#
#Takes an optional input path to append to the icloud directory
#
#Author = Brandon Tarney
#Verions = 1.0

import os
import time
import glob
import sys
import shutil

#Determine if a file is "recent enough" based on its input time
#input: timeToCompare: datae-time struct of time of file (from metadata)
def recentFile(timeToCompare):

	localtime = time.localtime()
	year = localtime.tm_year
	month = localtime.tm_mon
	day = localtime.tm_mday
	hour = localtime.tm_hour

	if (year != timeToCompare.tm_year
		or month != timeToCompare.tm_mon
		or day != timeToCompare.tm_mday
		or (hour - timeToCompare.tm_hour) > 1):
		return False

	return True


def main():
	downloadsPath = "/Users/Tarney/Downloads/"
	iCloudPath="/Users/Tarney/Library/Mobile Documents/com~apple~CloudDocs/"

	if sys.argv[1]:
		print "Program input: " + sys.argv[1]
		iCloudPath = iCloudPath + sys.argv[1]

	downloads = glob.glob(downloadsPath + "*")
	print ("here are all the downloads: ")
	print downloads

	print ("\n\n here are all the downloads within the last hour: ")
	recentFiles = [ paths for paths in downloads if recentFile(time.localtime(os.stat(paths).st_ctime)) ]
	print recentFiles

	for file in recentFiles:
		rootFileName = os.path.basename(file)
		print "File moved: " + rootFileName
		shutil.move(file, iCloudPath + rootFileName )

if __name__ == "__main__":
	main()
