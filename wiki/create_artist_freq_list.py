# Purpose: to create a clean list of all bands within each genre

from operator import itemgetter, attrgetter, methodcaller


sourceData = "./data/";
newData = "./newData/";
wikidump = "./wikidumps/"



output = ""

artistList = []

genre_list = set()
num_a_in_g = 0

with open(newData + "artists_list.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    for line in text:

        
        if line.find(" ****** ") != -1:
            
            print(line)
            print("#bands in this genres: " + str(num_a_in_g))
            genre_list.clear()
            # print("should be 0: " + str(len(genre_list)))
            num_a_in_g = 0
        else:
            num_a_in_g += 1
            # if ((len(genre_list) % 1000) == 0):
            #     print(str(len(genre_list)))
            genre_list.add(line)
            artistList.append(line)

print(len(artistList))

test = artistList[0:10000]



freq = [(item, test.count(item)) for item in set(test)]
print(len(freq)) 

# print(sorted(freq, key=itemgetter(1)))
        
        



# text_file = open(newData + "artists_list.txt", "w")
# text_file.write(output)
# text_file.close()
    		# searchResult = wikipedia.page(bandname)
    		# print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows

# with open(newData+"_languages_authority.json", "w", encoding="utf-8") as f:
#     json.dump(authorityDict, f, sort_keys=True, indent=4, ensure_ascii=False)

