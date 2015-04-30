#go from a list of coordinates and years to a list of coordinates and freqs




from collections import defaultdict
import csv

sourceData = "./locations/"


print("Lat, Long, num")

coords_list = []

with open(sourceData + 'noise_pre.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
    	if row[0] != "N, A" and int(row[1]) < 2017:
    		coords_list.append(row[0])

d = defaultdict(int)
for coord in coords_list:
    d[coord] += 1

# print(d)
for latlong in d:
	print(latlong + ", " + str(d[latlong]))
# print(d)