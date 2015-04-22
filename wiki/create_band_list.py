# Extract band name, year, and location
# 
# by Nick Usoff

## Plan - go through each info box, check if they are a "musical artist"
##        and if they are, add a line to the file with the name of the
##        article (artist name), year they were founded, and location
##        of where they were founded

import os, json, wikipedia, geopy


sourceData = "./data/";
newData = "/newData/";


with open(sourceData+"bandlist", "r", encoding="utf-8") as f: