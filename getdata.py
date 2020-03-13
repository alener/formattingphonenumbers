from pathlib import Path
from odf import text, teletype
from odf.opendocument import load

p = Path(".")

directories1 = [x for x in p.iterdir() if x.is_dir()]

textfiles = [list(p.glob("**/*.txt")), list(p.glob("**/*.odt"))]





numbers_from_odt = []

odtfiles = textfiles[1]
newodtfiles = []

for i in range(len(odtfiles)):
    file = str(odtfiles[i])
    newodtfiles.append(file)      #transform odtfiles in string list


for item in newodtfiles:
    doc = load(item)       #load all odt document with odf library

    allparas = doc.getElementsByType(text.P)
    for i in range(len(allparas)):
        numbers_from_odt.append(teletype.extractText(allparas[i]))   # put all numbers in a list

numbers_from_txt = []
for item in textfiles[0][1:]:
    sourceFile = open(str(item), "r")   # load all txt files
    for number in sourceFile:
        numbers_from_txt.append(number)   # put all numbers in a list
    sourceFile.close()

all_numbers = numbers_from_odt + numbers_from_txt   # add lists


allnumbersFile = open("allnumbers.txt", "w+")
for item in all_numbers:
    print(item[:-1], file=allnumbersFile)   # put all list item in a file with all data


allnumbersFile.close()
