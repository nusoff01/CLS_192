# The purpose of this file is to extract band names from the wikipedia
# article on the list of bands in a genre
import os, json, wikipedia


sourceData = "./data/";
newData = "/newData/";
print(wikipedia.search("Wikipedia"))

with open(sourceData+"bandlist", "r", encoding="utf-8") as f:
    text = f.read()
    text = text.split("\n")
    openBrace = "[[";
    closeBrace = "]]";
    sep = "|"
    for line in text:
    	if line.find(openBrace) == 2:
    		bandname = line[4:line.find(closeBrace)]
    		if bandname.find("|") != -1:
    			bandname = bandname[0:bandname.find("|")]

    		print("looking for " + bandname)
    		searchResult = wikipedia.page(bandname)
    		print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows

# with open(newData+"_languages_authority.json", "w", encoding="utf-8") as f:
#     json.dump(authorityDict, f, sort_keys=True, indent=4, ensure_ascii=False)

