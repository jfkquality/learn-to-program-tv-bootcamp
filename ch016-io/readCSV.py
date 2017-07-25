import csv #Import csv library

directory = open("createCSVFile.csv", "r")
try:
    reader = csv.reader(directory)
    for row in directory:
#        print row
        for item in row:
            print item
        print "\n"
finally:
    directory.close()
