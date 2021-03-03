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
data = open(args.swissprot,"r")

with data as f:
    content = f.readlines()
    for i in range(len(content) - 1):
        # Looking for 2 AC LINES IN A ROW, GET THEIR CONTENT INTO ONE LIST
        if content[i].rstrip().startswith("AC") and content[i+1].rstrip().startswith("AC"):
            ac1 = content[i].rstrip()[2:]
            acvalue1 = ac.split()
            ac2 = content[i+1].rstrip()[2:]
            acvalue2 = ac2.split()

            acvaluecombined = acvalue1 + acvalue2
        # IF ONLY 1 LINE WITH AC
        elif content[i].rstrip().startswith("AC") and not content[i+1].rstrip().startswith("AC"):
            ac = content[i].rstrip()[2:]
            acvalue = ac.split()
        # GET THE KEYWORD LINE
        if content[i].rstrip().startswith("KW"):       #get line with all keywords
            kw = content[i].rstrip()[2:]
            kw = kw.split(';')          #get all the keywords as a single string
            newkw=[]
            for element in kw:
                newkw.append(element.strip())   # to remove every symbol influencing the string
            for c in newkw:                #loops through all keywords in file
                c = c.replace(".", "")
                if c in keywords:       #if keyword in file is keyword we are looking for
                    if acvalue:
                        #print(acvalue)
                        for w in acvalue:
                            newac = w.replace(";", '')
                            AC.append(newac)
                    if not acvaluecombined:
                        print("'''acvaluecombined'''")
                        for w in acvalue2:
                            newac = w.replace(";", '')
                            AC.append(newac)

ac_sorted = list(set(AC))  #set so duplicates are removed

#for value in sorted(ac_sorted):
 #   print(value)
'''                 
ac_sorted = list(set(AC))  #set so duplicates are removed

for value in sorted(ac_sorted):
    print(value)

#print(len(AC))



#isEmpty = (len(matches) == 0)
            #if isEmpty:
             #   continue
            #else:
             #   for w in acvalue:
              #      newac = w.replace(";", '')
               #     AC.append(newac)


#for c in kw:
 #   c = c.replace(".", "")
  #  c = c.replace(" ", "")
   # if c in keywords:
    #    for w in acvalue:
     #       newac = w.replace(";", '')
      #      AC.append(newac)
      '''

