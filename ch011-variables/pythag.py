import math

a = input("What is the length of Side A?: ")
b = input("What is the length of Side B?: ")
c = a*a + b*b

print "The length of the hypotenuse of a right triangle where Side A = {} and Side B = {} is {}.".format(a, b, math.sqrt(c))

