                                           #Description

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

 

Programming language - any. Instruction how to run should be provided along with the solution.