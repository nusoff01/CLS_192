# The purpose of this script is to take in a band list (i.e. band name, 
#	year founded, and town founded in) and convert the town founded in 
#   to coordinates


import geopy, csv

sourceData = "./csvs/"


from geopy.geocoders import Nominatim
geolocator = Nominatim()

# location = geolocator.geocode("Montreal, Quebec, Canada")
# print((location.latitude, location.longitude))

with open(sourceData + 'noise.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        town_loc = row[0]
        town_loc = town_loc.replace("U.S.", "United States")
        coords = geolocator.geocode(town_loc, timeout=10)
        try:
        	row[0] = (coords.latitude, coords.longitude)
        except:
        	row[0] = "NA"
        print('"' + str(row[0][0]) + ", " + str(row[0][1]) + '", ' + str(row[1]))