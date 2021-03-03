#!/usr/bin/python3
import argparse
import itertools
"""
USAGE OF SCRIP: --keyword <keyword> <keyword> ... --swissprot swissprot45.dat
STILL TO CHECK: 
# case 4: special case: more than one AC line per entry
3D-structure
# case 6: special case: keyword contained in other keywords
Signal
# case 12: 

"""

parser = argparse.ArgumentParser()
parser.add_argument("--keyword", dest="keywords", nargs='*')  #read in any flexible num of args
parser.add_argument("-swissprot", "--swissprot")

args = parser.parse_args()

keywords = args.keywords


AC=[]


with open(args.swissprot) as data:
    for line in data:
        if line.startswith("AC"):
            ac = line[2:]               #get line with ac numbers
            acvalue = ac.split()        #store the values of all ac numbers as a list of single strings
            #print(acvalue)
            nextline = next(data, '').strip()
            if nextline.startswith("AC"):
                line2 = nextline
                ac = line2[2:]
                #print(ac)
                acvalue2 = ac.split()
                #print(acvalue2)
            #print(acvalue)
        if line.startswith("KW"):       #get line with all keywords
            kw = line[2:]
            kw = kw.split(';')          #get all the keywords as a single string
            #print(kw)
            newkw=[]
            for element in kw:
                newkw.append(element.strip())   # to remove every symbol influencing the string
            for c in newkw:                #loops through all keywords in file
                c = c.replace(".", "")
                if c in keywords:       #if keyword in file is keyword we are looking for
                    #print(acvalue)
                    print(acvalue2)
                    for w in acvalue:
                        newac = w.replace(";", '')
                        AC.append(newac)

ac_sorted = list(set(AC))  #set so duplicates are removed

for value in sorted(ac_sorted):
    print(value)
