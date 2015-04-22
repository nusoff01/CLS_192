# PUT FILE COMMENTS HERE


import geopy, csv, re 

sourceData = "wikidumps/"




# given a portion of an infobox likely to contain the origin of a band, 
# return the origin, or "NF" if not found

def extract_origin(text):
    end_o = text.find("\\n")
    o_text = "NF"
    if end_o != -1:
        o_text = text[0:end_o]
    if o_text.find("<") != -1:
        start_com = o_text.find("<");
        end_com = o_text.find(">");
        if end_com == -1:
            return "NF"
        com_string = (o_text[start_com:(end_com+1)])
        o_text = o_text.replace(com_string, " ")
        # print("DIDTHISWORK")
        # print("to be removed: |" + com_string + "|")
    start_real_o = o_text.find("=")
    if start_real_o == -1:
        return "NF"

    o_text = o_text[(start_real_o + 2):]
    if len(o_text) < 3:
        return "NF"

    bar_loc = o_text.find("|")
    if bar_loc != -1:
        o_text = o_text[0:bar_loc]
    return o_text

# given a portion of an infobox likely to contain the first active year of a band,
# return the year, or "NF" if not found

def extract_start(text):
    end_y = text.find("\\n")
    y_text = "NF"
    if end_y != -1:
        y_text = text[0:end_y]

             
    number_length = 4                                   
    pattern= r"\D(\d{%d})\D" % number_length   # \D to avoid matching 567           
    years = re.findall(pattern, y_text)
    if len(years) == 0:
        return "NF"
    return years[0]


# location = geolocator.geocode("Montreal, Quebec, Canada")
# print((location.latitude, location.longitude))

with open(sourceData+"Ambient_dump.txt", "r", encoding="latin-1") as f:
    text = f.read()
    
    openBrace = "[[";
    closeBrace = "]]";
    sep = "|";
    ibox_string = "Infobox musical artist"
    

    infobox_count = 0
    infobox_start = 0;
    while infobox_start != -1:
        infobox_start = text.find(ibox_string);
        if infobox_start != -1:
            text = text[(infobox_start + 1):]
            orig_start = text.find("origin");
            year_start = text.find("years_active")
            next_info = text.find(ibox_string);

            orig_text = "NF"
            year_text = "NF"
            valid_box = 0; #if this is two at the end, box is valid

            if (orig_start < next_info) and (orig_start != -1):
                orig_text = extract_origin(text[orig_start:(orig_start + 125)])
                if orig_text != "NF":
                    
                    orig_text = orig_text.replace("[", "")
                    orig_text = orig_text.replace("]", "")
                    valid_box += 1
                    # infobox_count += 1
            if (year_start < next_info) and (year_start != -1):
                year_text = extract_start(text[year_start:(year_start + 100)])
                if year_text != "NF":
                    valid_box += 1
            if valid_box == 2:
                print("\"" + orig_text + "\"" + ", " + year_text)
                infobox_count += 1



print(infobox_count)


