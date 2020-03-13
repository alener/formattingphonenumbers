"""Description

 Write an application that finds all phone numbers in a set of text files located in a directory 
 tree starting with <somewhere>. Files should be processed regardless of the nesting level.
  At the same time, only text files with .txt extension need to be processed,
and the others should be ignored. Phone numbers in the source files can be given with the country code:

+7 812 number

+7 (495) number

+7812number

+7812 number

7-812-number



With a three-digit area code:

(812) number

812number

812 number

095-number

+7 (883) 87-01346
+1649948-67575
+71 659 2082817
+94270 6205785
98-629-4570911

565 9779732
224-6518945
3477489

Or none at all. At the same time the number can have different spellings:

123-4567

123-45-67

1234567

 

If the city code is not specified, it is considered equal to 812, if the country code is not specified, 
it is considered equal to 7. 
You need to find all the numbers in all of the files. Change formatting to the unified "full" format

+7 (812) 123-4567

remove duplicates and print the list of numbers in ascending order.

 

Programming language - any. Instruction how to run should be provided along with the solution."""


from random import sample


def populate_files(n, sourceFile):  # populate txt files with the format required

    first_part = sample(range(1, 100), k=n)

    second_part = sample(range(100, 1000), k=n)

    third_part = sample(range(1000000, 10000000), k=n)  # generating random numbers

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
        elif i % 8 == 2:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(
                "+", plus, " ", parenthesis, " ", phonenumber, sep="", file=sourceFile
            )
        elif i % 8 == 3:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print("+", plus, parenthesis, " ", phonenumber, sep="", file=sourceFile)
        elif i % 8 == 4:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            plus = str(first_part[i])
            print(plus, "-", parenthesis, "-", phonenumber, sep="", file=sourceFile)

        elif i % 8 == 5:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            print(parenthesis, phonenumber, file=sourceFile)
        elif i % 8 == 6:
            phonenumber = str(third_part[i])
            parenthesis = str(second_part[i])
            print(parenthesis, "-", phonenumber, file=sourceFile, sep="")
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

    sourceFile.close()


from pathlib import Path

p = Path(".")

directories1 = [x for x in p.iterdir() if x.is_dir()]

textfiles = [
    list(p.glob("**/*.txt")),
    list(p.glob("**/*.odt")),
]  # all kinds of files in the current directory


files = []
for item in textfiles[0]:
    item = str(item)
    files.append(item)


for (
    item
) in files:  # populating files in this directory with all kinds of format numbers.
    populate_files(n=80, sourceFile=item)
