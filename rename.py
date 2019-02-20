import os

currentfilename = ""
newfilename = ""
workingdirectory = ""
i = input("How many files / How many times loop with occur: ")
print("old file name info")
b = input("starting filename (like \"a(\" -- in \"a(1).jpeg'\": ")
a = input("a starting integer that all files have different (like 1)-- in \"a(1).jpeg'\": ") 
c = input("ending file name / extension (like ).jpg)-- in \"a(1).jpeg'\": ")
print("new file name info")
d = input("Starting file name: ")
e = input("Ending file name: ")
a = int(a)
i = int(i)

while a < i:
	a = str(a)
	os.rename(b + a + c, d + a + e)
	a = int(a)
	a = a + 1