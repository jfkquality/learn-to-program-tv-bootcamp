import numpy

print "Please eter the list of student names and correspondiing GPAs."

studentGPAs = {}
name = raw_input("Student Name [x to exit] :")
while ( name.upper() != 'X'):
        gpa = raw_input("Student GPA: ")
        studentGPAs[name] = float(gpa)
        name = raw_input("Student Name [X to exit] :")
total = 0
avg = 0
#if len(studentGPAs) > 0:
#    for name in studentGPAs:
#        total = total + studentGPAs[name]
#    avg = total / len(studentGPAs)
for name, gpa in studentGPAs.items():
    print "{} : {}".format(name, gpa)
print "Average: ", numpy.mean(studentGPAs.values())
print "High", numpy.max(studentGPAs.values())
print "Low", numpy.min(studentGPAs.values())
print "Median: ", numpy.median(studentGPAs.values())

