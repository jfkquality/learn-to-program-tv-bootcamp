myFile = open("poem.txt", "r+")
#poem = myFile.read() # use read() method to read
poem2 = myFile.read(5)
position = myFile.tell()
print "Position of the file pointer: ", position
#print poem
print poem2
myFile.close()
