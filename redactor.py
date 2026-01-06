import sys
import glob
import spacy
import re
import os
from commonregex import CommonRegex
#import spacy.cli

#spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

bl_char = '\u2588'

a=[]
a=sys.argv      
path = ''
redacted_path = ''
status = ''
# flag = []
# print(flag)
#print(a)

for i in range(1, len(sys.argv), 2):
    if sys.argv[i] == '--input':
        path = sys.argv[i+1]
    elif sys.argv[i] == '--output':
        redacted_path = sys.argv[i+1]
    elif sys.argv[i] == '--stats':
        status = sys.argv[i+1]

#print(a)
files_list=glob.glob(path)

n = "names"
d= "dates"
p ="phones"
g = "genders"
ad = "address"



def names_red(text):
    # doc = nlp(text)
    # red_text = text
    # count = 0
    # for ent in doc.ents:
    #     if ent.label_ == "PERSON":
    #         count+=1
    #         red_text = red_text.replace(ent.text,bl_char*len(ent.text))
    # return [red_text, count]
    doc = nlp(text)
    count = 0
    n_list = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            count += 1
            n_list.append(ent.text)
    #print(matches)        
    return n_list, count
 

def red_date(text):
    data = CommonRegex(text)
    d_list = data.dates
    # for s in stext:
    #     if s in text:
    #         text=text.replace(s,bl_char*len(s))
    #return text, len(stext)
    return d_list, len(d_list)
    

def red_phnum(data):
    phone_pattern = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    ph_list = re.findall(phone_pattern,data)
    count = len(ph_list)
    # data = phone_pattern.sub(bl_char * 10, data)
    # return [data,count]
    return ph_list, count


def red_gender(text): 
    terms = ["wife", "husband", "Husband", "Wife", "Mr","Ms","Miss","Mrs","He"," he ","Him"," him ", "His", " his ","She"," she ","Her", " her ", "Father", "father", "daughter", "Mother", "mother", "Brother", "brother", "Sister", "sister", "Uncle", "Aunt", "aunt", "Grandfather", "Grandmother","grand father", "grand mother"]
    #redacted_text = text
    g_list = []
    count = 0
    for token in terms:
        if token in text:
            count+=1
            g_list.append(token)
    #         redacted_text = redacted_text.replace(token,bl_char*len(token))        
    # return [redacted_text, count]
    return g_list, count
  


def red_add(data):
    parsed_text = CommonRegex(data)
    stad_list = parsed_text.street_addresses
    #print(st_address)
    # for st in st_address:
    #     if st in data:
    #         data = data.replace(st,bl_char*len(st))
    return stad_list, len(stad_list)

def redaction(nlist,glist,dlist,adlist,phlist,data):
    t_list = nlist+glist+dlist+adlist+phlist
    fdata = data
    cnt = 0
    for st in t_list:
            if st in fdata:
                cnt += 1
                fdata = fdata.replace(st,bl_char*len(st))
    return fdata, cnt           

    
    

for filename in files_list:
    print("Status for the file ",filename)
    with open(filename, "r") as f:
        text = f.read()
        status = ''

        if '--names' in a:
              n_list, ncount = names_red(text) # returns n_list and count
              if(ncount==0):
                status += "There are no names in the file \n"
              else:
                status += "The names that are redacted : "
                status += str(ncount) + "\n"
        else:
            n_list = []
            ncount = 0        
        if '--genders' in a:
            g_list, gcount = red_gender(text)  # returns g_list, count
            if(gcount==0):
              status += "There are no genders in the file \n"
            else:
              status += "The number of genders that are redacted : "
              status += str(gcount) + "\n"
        else:
            g_list = []
            gcount = 0      
        if '--dates' in a:
            date_list, dcount= red_date(text) #returns date_list,count
            if(dcount==0):
              status += "There are no dates in the file \n"
            else:
              status += "The number of dates that are redacted : "
              status += str(dcount) + "\n"
        else:
            date_list = []
            dcount = 0      
        if '--phones'  in a:
            num_list,adcount = red_phnum(text) #returns num_list,count
            if(adcount==0):
              status += "There are no phone numbers in the file \n"
            else:
              status += "The number of phone numbers that are redacted : "
              status += str(adcount) + "\n"
        else:
            num_list = []
            adcount = 0      
        if '--address' in a:
            ad_list,cnt = red_add(text) #returns ad_list,count
            if(cnt==0):
                status += "There are no addresses in the file \n"
            else:
                status += "The number of addresses that are redacted : "
                status += str(cnt) + "\n"
        else:
            ad_list = []
            cnt = 0        
        #print(status)    
        finaldata, totalcount = redaction(n_list,g_list,date_list,num_list,ad_list,text)
        str1= filename+'.redacted'
        
        with open(str1, "w", encoding="utf-8") as file:
            file.write(finaldata)
            file.close()
            
    
    sys.stderr.write(status+ "\n")
        

