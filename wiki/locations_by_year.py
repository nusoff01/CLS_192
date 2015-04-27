# The purpose of this script is to take in a band list (i.e. location 
#	and town founded in) and extract the locations after a given date


import csv

sourceData = "csvs/"




cutoff_year = 2016

with open(sourceData + 'House.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        year_founded = row[1]
        if int(year_founded) < cutoff_year:
        	print (row[0])