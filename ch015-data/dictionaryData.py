gpas = {
    "Mark" : 3.56,
    "Fred" : 2.99,
    "John" : 3.99,
    "Mary" : 2.55,
    "Lois" : 3.15,
    "Brett" : 1.0
    }

print gpas

print "The GPA is: ", (gpas["Mark"])

# Change Lois
gpas["Lois"] = 2.96
print gpas["Lois"]

# Add 
gpas["Thomas"] = 3.1
print gpas["Thomas"]

# Delete
del gpas["Fred"]
print gpas

#Reference
if gpas.has_key("Mark"):
    print "Mark is here"

if gpas.has_key("Fred"):
    print "Fred is here"
else:
    print "Fred has left the building"

print gpas.keys()
print gpas.values()

print len(gpas)
