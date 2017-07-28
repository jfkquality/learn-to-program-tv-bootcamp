# 7A, 7B
def range (num1, num2, step):
    x = num1
    if num1 < num2:
        while x <= num2:
            print x
            x = x + step
    else:
        while x >= num2:
            print x
            x = x - step

# Problem 7A
print "Problem 7A"
print ""
range(0, 100, 5)

# Problem 7B
print "Problem 7B"
print ""
range(1000, 950, 1)

# Problem 7C
members = ["Mark", "Jay", "Tom", "Mary", "Kathy", "Donald"]
for name in members:
    print name
