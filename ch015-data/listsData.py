names = ["Mark", "Fred", "Tom", "Wendy", "Kevin" ]
gpas = [ 3.41, 2.55, 4.0, 2.95, 3.75 ]

print names[0]
print names[3]
names.append("Brett")
print names[5]
del names[5]

print gpas[2]
print gpas[4]

print names

for name in names:
    print name
    
for score in gpas:
    print score

