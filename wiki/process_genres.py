# Purpose: to create a clean list of all bands within each genre


sourceData = "./data/";
newData = "./newData/";
wikidump = "./wikidumps/"



output = ""

with open(wikidump + "Genre_dump.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    collecting = True; #flag for whether or not looking for artists
    for line in text:

        
        if line.find(" ****** ") != -1:
            collecting = True;
            print(line)
            output += line + "\n"
        if line.find("==See also==") != -1:
            collecting = False;
        if collecting:
            if line.find("List of") != -1:
                continue
            if((line.find("*[[") != -1) or 
               (line.find("* [[") != -1) or 
               (line.find("| [[") != -1) or 
               (line.find("|[[") != -1)):
                
                start_index = line.find("[[")

                line = line[(line.find("[[") + 2):]
                end_index = line.find("]]")
                split_index = line.find("|")

                if ((split_index != -1) and (split_index < end_index)):
                    output += line[:split_index] + "\n"
                else:
                    output += line[: line.find("]]")] + "\n"

text_file = open(newData + "artists_list.txt", "w")
text_file.write(output)
text_file.close()
    		# searchResult = wikipedia.page(bandname)
    		# print(str(searchResult.content))
        # input(authorityDict) # uncomment this line to see how authorityDict() grows

# with open(newData+"_languages_authority.json", "w", encoding="utf-8") as f:
#     json.dump(authorityDict, f, sort_keys=True, indent=4, ensure_ascii=False)

