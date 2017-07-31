import csv

directory = open("directory.csv", "wb")
selection = ""

def showMenu():
    print "A) Add to Directory"
    print "B) Display Directory"
    print "X) Exit Directory Program"
#    return selection
    
def addEntry(fname, lname, email, phone):
    directory = open("directory.csv", "a")
    directory.write(firstName + ",")
    directory.write(lastName + ",")
    directory.write(email + ",")
    directory.write(phone + "\n")
    print "{} {} added to the directory".format(fname, lname)
    directory.close()

def printDirectory():
    contactList = open("directory.csv", "r")
    print "Display Directory"
#    reader = csv.reader(csvFile)
    reader = csv.reader(contactList)
    try:
        for row in reader:
#            print row
            for item in row:
                print item,
            print "\n"
    finally:
        contactList.close()
    
while (selection.upper() != "X"):
    showMenu()
    selection = raw_input("--")
    if (selection.upper() == "A"):
            print "Add to Directory"
            firstName = raw_input("First Name: ")
            lastName = raw_input("Last Name: ")
            email = raw_input("Email: ")
            phone = raw_input("Phone: ")
            addEntry(firstName, lastName, email, phone)
    elif (selection.upper() == "B"):
            printDirectory()

