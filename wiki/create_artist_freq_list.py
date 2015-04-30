# Purpose: to create a clean list of all bands within each genre

from operator import itemgetter, attrgetter, methodcaller


sourceData = "./data/";
newData = "./newData/";
wikidump = "./wikidumps/"



# musicians 
# artists
# bands
# performers
# bands and artists
# musicians and groups
# artists and bands
# pianists


# BAD:
 # ****** List of black metal bands, 0-K
 # ****** List of black metal bands, L-Z
 # ****** List of blues musicians
 # ****** List of death metal bands
 # ****** List of disco artists
 # ****** List of disco artists (A-E)
 # ****** List of disco artists (F-K)
 # ****** List of disco artists (L-R)
 # ****** List of disco artists (S-Z)
 # ****** List of glam punk artists       - {{flagicon...}}
 # ****** List of heavy metal bands
 # ****** List of Japanoise artists
 # ****** List of mathcore bands
 # ****** List of metalcore bands
 # ****** List of post-grunge bands
 # ****** List of rai musicians
 # ****** List of R&B musicians




output = ""
genre_name = ""

artistList = []

genre_list = []
num_a_in_g = 0

with open(newData + "artists_list.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    for line in text:

        
        if line.find(" ****** ") != -1:
            print("#bands in this genre: " + str(num_a_in_g))
            genre_name =  '"' + line.split("List of ",1)[1] + '"'
            print(line)
            
            # print("should be 0: " + str(len(genre_list)))
            num_a_in_g = 0
        else:
            line = '"' + line + '"'
            if(len(line) > 0):
                try:
                    dict(genre_list)[line].add(genre_name)
                except KeyError:
                    genre_list.append((line, {genre_name}))
                num_a_in_g += 1
                # if ((len(genre_list) % 1000) == 0):
                #     print(str(len(genre_list)))
                # genre_list.add(line)
                artistList.append(line)

print(len(artistList))

test = artistList


# print(genre_list)

print([len(x[1]) for x in genre_list])

for x in genre_list:
    print(x[0] + ", " + str(x[1]))
# freq = [(item, test.count(item)) for item in set(test)]
# print(freq)
# print(len(freq)) 

# print(sorted(freq, key=itemgetter(1)))
        
        



# text_file = open(newData + "artists_list.txt", "w")
# text_file.write(output)
# text_file.close()
    		# searchResult = wikipedia.page(bandname)
    		# print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows

# with open(newData+"_languages_authority.json", "w", encoding="utf-8") as f:
#     json.dump(authorityDict, f, sort_keys=True, indent=4, ensure_ascii=False)

