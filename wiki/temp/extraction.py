# extract the corner cases of genre list dumps

# Purpose: to create a clean list of all bands within each genre


sourceData = "./data/";
newData = "./newData/";
wikidump = "./wikidumps/"



output = ""

with open(wikidump + "Genre_dump.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    for line in text:

        
        if line.find(" ****** ") != -1:
            print(line)
            output += line + "\n\n"
        if((line.find("| [[") != -1) or (line.find("* [[") != -1)):

            end_index = line.find("]]")
            split_index = line.find("|")

            if ((split_index != -1) and (split_index < end_index)):
                output += line[(line.find("[[") + 2): split_index] + "\n"
            else:
                output += line[(line.find("[[") + 2): line.find("]]")] + "\n"


        
    
text_file = open("./artists_list_blues.txt", "w")
text_file.write(output)
text_file.close()
    		

