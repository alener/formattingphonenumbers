from generatedata import files

# wrapper in a function for testability purposes
def format_data():
    """ Formatting data in a required format"""
    phonenumbers = []
    for item in files:
        sourceFile = open(item, "r")  # open files for read

        for x in sourceFile:
            onlydigit = ""
            for y in x:
                if y.isdigit():  # check character isdigit
                    onlydigit = onlydigit + y
            if len(onlydigit) == 7:
                onlydigit = (
                    "7812" + onlydigit
                )  # complete digits with required numbers prefix
            if len(onlydigit) == 10:
                onlydigit = (
                    "7" + onlydigit
                )  # complete digits with required numbers prefix
            phonenumbers.append(onlydigit)  # put all numbers in a list
        sourceFile.close()
        phonenumbersunique = set(
            phonenumbers
        )  # in order to remove duplicates transform list in a set
        phonenumbers = list(phonenumbersunique)  # come back to be a list
        phonenumbers.sort(key=int)  # sort list with numbers

    finallist = []
    for onlydigit in phonenumbers:

        if len(onlydigit) == 11:  # formating numbers with required final format
            finalnumber = [
                "+",
                onlydigit[0],
                " (",
                onlydigit[1:4],
                ") ",
                onlydigit[4:7],
                "-",
                onlydigit[7:],
            ]
            finalphonenumber = "".join(finalnumber)
            finallist.append(finalphonenumber)
        if len(onlydigit) == 12:  # formating numbers with required final format
            finalnumber = [
                "+",
                onlydigit[:2],
                " (",
                onlydigit[2:5],
                ") ",
                onlydigit[5:8],
                "-",
                onlydigit[8:],
            ]
            finalphonenumber = "".join(finalnumber)
            finallist.append(finalphonenumber)  # put all numbers formatted in a list

    destinyFile = open("ouputs/formatednumbers.txt", "w+")
    count = 0
    for item in finallist:
        print(item, file=destinyFile)  # put lists items in the destiny file
        count = count + 1
    destinyFile.close()

    return count


format_data()

if __name__ == "__main__":

    format_data()
