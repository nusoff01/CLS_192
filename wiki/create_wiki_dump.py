# The purpose of this file is to extract band names from the wikipedia
# article on the list of bands in a genre
import pycurl
from io import BytesIO
import unicodedata
import urllib



sourceData = "./data/";
newData = "./newData/";
wikidump = "./wikidumps/"


pre_url = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles="
pre_url = "http://en.wikipedia.org/w/index.php?action=raw&title="


post_url = "&rvsection=0"


c = pycurl.Curl()

buffer = BytesIO()



c = pycurl.Curl()




c.setopt(c.WRITEDATA, buffer)
body = ""

with open(sourceData+"genre_lists.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    for line in text:

        print(line)
        # print(unicodedata.normalize('NFKD', line).encode('ascii', 'ignore'))
        # print(sutf8.decode('unicode-escape'))
        # open('utf-8.out', 'w').write(sutf8)

        url = pre_url + line

        buffer = BytesIO()
        # print(line)
        c.setopt(pycurl.URL, url.encode('utf-8'))
        c.setopt(c.WRITEDATA, buffer)
        c.perform()

        raw_body = str(buffer.getvalue())
        
        body += "\n\n ****** " + line.replace("%20", " ") + "\n\n";
        body += raw_body.replace("\\n", "\n")


        
        



text_file = open(wikidump + "Genre_dump.txt", "w")
text_file.write(body)
text_file.close()
    		# searchResult = wikipedia.page(bandname)
    		# print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows

# with open(newData+"_languages_authority.json", "w", encoding="utf-8") as f:
#     json.dump(authorityDict, f, sort_keys=True, indent=4, ensure_ascii=False)

