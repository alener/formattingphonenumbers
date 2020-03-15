from generatedata import textfiles
from odf import text, teletype
from odf.opendocument import load
from pathlib import Path

numbers_from_odt = []

odtfiles = textfiles[1]
newodtfiles = []


for i in range(len(odtfiles)):
    file = str(odtfiles[i])
    newodtfiles.append(file)  # transform odtfiles in string list


for item in newodtfiles:
    doc = load(item)  # load all odt document with odf library

    allrows = doc.getElementsByType(text.P)
    for i in range(len(allrows)):
        numbers_from_odt.append(
            teletype.extractText(allrows[i])
        )  # put all numbers in a list


numbers_from_txt = []
for item in textfiles[0]:
    sourceFile = open(str(item), "r")  # load all txt files
    for number in sourceFile:
        numbers_from_txt.append(number)  # put all numbers in a list
    sourceFile.close()

    all_numbers = numbers_from_odt + numbers_from_txt  # add lists

# wrapper in a function for testability purposes
def get_all_data():
    """  Get all phonenumbers for all files in a data directory """

    allnumbersFile = open("ouputs/allnumbers.txt", "w+")
    count = 0
    for item in all_numbers:
        count = count + 1
        print(
            item[:-1], file=allnumbersFile
        )  # put all list item in a file with all data

    allnumbersFile.close()
    return count


get_all_data()

if __name__ == "__main__":
    get_all_data()
