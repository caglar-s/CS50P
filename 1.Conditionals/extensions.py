"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""


filename = input("File name: ")
lwrfilename = filename.lower()

if ".gif" in lwrfilename:
    print("image/gif")
elif "jpg" in lwrfilename:
    print("image/jpeg")
elif "jpeg" in lwrfilename:
    print("image/jpeg")
elif "png" in lwrfilename:
    print("image/png")
elif "pdf" in lwrfilename:
    print("application/pdf")
elif "txt" in lwrfilename:
    print("text/plain")
elif "zip" in lwrfilename:
    print("application/zip")
else:
    print("applications/octet-stream")
    