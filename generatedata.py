from pathlib import Path
from random import sample


def populate_files(n, sourceFile):
    """ populate txt files with the format required"""

    first_part = sample(range(1, 100), k=n)

    second_part = sample(range(100, 1000), k=n)

    third_part = sample(range(1000000, 10000000), k=n)  # generating random numbers
    count = 0
    sourceFile = open(sourceFile, "w+")
    for i in range(len(third_part)):  # formating numbers in diferents ways required
        if i % 8 == 0:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(
                "+",
                plus,
                " (",
                parenthesis,
                ") ",
                phonenumber[:2],
                "-",
                phonenumber[2:],
                sep="",
                file=sourceFile,
            )
            count = count + 1
        elif i % 8 == 1:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(
                "+",
                plus,
                parenthesis,
                phonenumber[:2],
                "-",
                phonenumber[2:4],
                "-",
                phonenumber[4:],
                sep="",
                file=sourceFile,
            )
            count = count + 1
        elif i % 8 == 2:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(
                "+", plus, " ", parenthesis, " ", phonenumber, sep="", file=sourceFile
            )
            count = count + 1
        elif i % 8 == 3:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print("+", plus, parenthesis, " ", phonenumber, sep="", file=sourceFile)
            count = count + 1
        elif i % 8 == 4:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(plus, "-", parenthesis, "-", phonenumber, sep="", file=sourceFile)
            count = count + 1
        elif i % 8 == 5:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            print(parenthesis, phonenumber, file=sourceFile)
            count = count + 1
        elif i % 8 == 6:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            print(parenthesis, "-", phonenumber, file=sourceFile, sep="")
            count = count + 1
        else:
            phonenumber = str(third_part[i])
            print(
                phonenumber[:2],
                "-",
                phonenumber[2:4],
                "-",
                phonenumber[4:],
                sep="",
                file=sourceFile,
            )
            count = count + 1
    sourceFile.close()
    return count


p = Path("data")

directories1 = [x for x in p.iterdir() if x.is_dir()]

textfiles = [
    list(p.glob("**/*.txt")),
    list(p.glob("**/*.odt")),
]  # all kinds of files in the current directory


files = []
for item in textfiles[0]:
    item = str(item)
    files.append(item)

if __name__ == "__main__":
    for (
        item
    ) in files:  # populating files in this directory with all kinds of format numbers.
        print(populate_files(n=80, sourceFile=item))

# map(populate_files(n=80),files)
