def greetPerson(name):
    "This function greets the user by name."
    print "Greetings", name

personName = raw_input("What is your name? ")
greetPerson(personName)

def addThese(a, b):
    "Add two numbes together"
    c = a + b
    print c

addThese(10, 15)

family = ["Mark", "Brett", "Kerry", "Joan", "Rick", "Rose"]

def printFirst(myList):
    print myList[0]

printFirst(family)
