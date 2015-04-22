# The purpose of this script is to take in a band list (i.e. band name, 
#	year founded, and town founded in) and convert the town founded in 
#   to coordinates


import geopy, csv

sourceData = "data/"


from geopy.geocoders import Nominatim
geolocator = Nominatim()




# location = geolocator.geocode("Montreal, Quebec, Canada")
# print((location.latitude, location.longitude))

with open(sourceData + 'bandlist.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        town_loc = row[2]
        town_loc = town_loc.replace("[", "")
        town_loc = town_loc.replace("]", "")
        coords = geolocator.geocode(town_loc)
        row[2] = (coords.latitude, coords.longitude)
        print(row)