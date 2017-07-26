import csv #Import csv library

directory = open("CSVFile.csv", "r")
try:
    reader = csv.reader(directory)
    for row in reader:
        print row
        for item in row:
            print item
        print "\n"
finally:
    directory.close()
