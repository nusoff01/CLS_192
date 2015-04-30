# go form bands to locations within a genre

import csv
import pycurl
from io import BytesIO
import unicodedata
import urllib


sourceData = "./"


pre_url = "http://en.wikipedia.org/w/index.php?action=raw&title="

artist_list = []

genre1 = "noise musicians"
genre2 = "country rock musicians"

with open(sourceData + 'artist_genre_freq.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in reader:
        for genre in row:
            if(genre.find(genre1) != -1):
                artist_list.append(row[0])

    	# artist_list.append(row[0])



c = pycurl.Curl()

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.WRITEDATA, buffer)
body = ""


counter = 0
for artist in artist_list:
    counter = counter + 1
    if (counter % 100 == 0):
        print(counter) 

    artist = artist.replace("&", "%26")
    url = pre_url + artist.replace(" ", "%20")

    buffer = BytesIO()
    # print(line)
    c.setopt(pycurl.URL, url.encode('utf-8'))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()

    raw_body = str(buffer.getvalue())
    
    body += "\n\n ****** " + artist + "\n\n";
    body += raw_body.replace("\\n", "\n")



text_file = open("./wikidumps/" + "dump_noise.txt", "w")
text_file.write(body)
text_file.close()
