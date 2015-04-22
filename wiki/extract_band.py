# The purpose of this file is to extract band names from the wikipedia
# article on the list of bands in a genre
import os, json, wikipedia


sourceData = "./data/";
newData = "/newData/";




with open(sourceData+"bandlist_Ambient", "r", encoding="ascii") as f:
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

    		print((bandname))



    		# searchResult = wikipedia.page(bandname)
    		# print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows



