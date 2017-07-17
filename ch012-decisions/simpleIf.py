age = input("How old are you? ")
citizen = raw_input("Are you a citizen (Y/N)? ")
if age >= 18 and citizen.upper() == "Y":
    print "You are eligble to vote in the USA"
    print "Congratulations."
else:
    print "You are not eligble to vote in the USA."
print "End of Program"

if age == 65:
    print "You are eligible for Social Security"

