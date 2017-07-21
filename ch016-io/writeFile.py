# First create a file pointer. Why call it a "pointer"? We're creating the FILE.
# Created in the folder where the py script is stored.
# Mode =
# - r read, (not correct for opening a file to write)
# - r+ read/write (not correct for opening a file to write),
# - w write,
# - b binary,
# - a append
myFile = open("family.txt", "wb")
myFile.write("Mark\n")
myFile.write("Joan\n")
myFile.write("Brett\n")
myFile.write("Kerry\n")
myFile.write("Rose\n")
myFile.write("Rick\n")
print "Just wrote the file: ", myFile.name
print "Opened file in mode: ", myFile.mode
myFile.close()

