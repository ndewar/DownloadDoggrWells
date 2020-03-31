# -*- coding: utf-8 -*-
"""
Created on Tues March 31, 2020
@author: Noah Dewar
takes in the results text file output from the DOGGR well finder web application (https://maps.conservation.ca.gov/doggr/wellfinder/) and the codes for
the counties you want to look in and downloads all of the files for those wells into the current folder
"""

# import the packages we need
import ftplib
from ftplib import FTP
import pandas as pd

def getData(folders):
	# need this stupid string
	s='/'

	for folder in folders:

		print(folder)
		# drop into the folder and get the sub folders
		ftp.cwd(s.join([folder,'']))
		filenames = ftp.nlst()

		# for each API in the results, check to see if there is a match in the current set of subfolders
		# if so, drop into it
		for name in results.API.astype(str):
			if name in filenames:
				print(s.join([name,'']))
				ftp.cwd(s.join([name,'']))

				# get list of files in the sub folder
				sub_filenames=ftp.nlst()
				for sub_name in sub_filenames:

					# do something different for the tifs folder, drop into it and copy all files
					print(sub_name)
					if sub_name.lower()=='tifs':
						ftp.cwd(s.join([sub_name,'']))
						subsub_filenames=ftp.nlst()
						if subsub_filenames==['No logs for this well']:
							print('No logs for this well')
						else:
							for subsub_name in subsub_filenames:
								print(subsub_name)
								file = open(subsub_name, 'wb')
								ftp.retrbinary('RETR '+ subsub_name, file.write)
								file.close()
						ftp.cwd('../')
					else:
						try:
							file = open(sub_name, 'wb')
							ftp.retrbinary('RETR '+ sub_name, file.write)
							file.close()
						except:
							print(sub_name,' did not work for some reason')
				ftp.cwd('../')
		ftp.cwd('../')
	return 

# read in the results csv that has the API numbers we want
# UPDATE THIS WITH YOUR FILENAME
results=pd.read_csv('results_trimmed.csv',dtype=object)

# login to the DOGGR ftp
ftp = FTP('ftp.consrv.ca.gov')    
ftp.login()                     
ftp.cwd('pub/oil/WellRecord/')  

# set which folders to look in, to look up the numbers for the counties you are interested in, navigate to this site:
# https://desktop.arcgis.com/en/arcmap/latest/extensions/business-analyst/counties.htm
# and take the last 3 digits of the county FIPS code.

# these codes are for Fresno, Tulare, and Kings counties
# UPDATE THIS WITH YOUR COUNTIE CODES
CountyNumbers=['019','107','031']

# this will download all of the files for the wells with API numbers in the results_trimmed.csv given above
# the first two digits must be trimmed off of the API numbers given in the original results file for them to match
# the folder numbers on the ftp server.
getData(CountyNumbers)