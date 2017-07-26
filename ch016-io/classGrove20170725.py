def square(length, width):
    area = length * width
    print area

square(5,6)
square(4.25, 6.7)

def triangle (height, base):
    area = .5 * base * height
    return area

shape = triangle(3, 4)
print shape

length = input("Enter length")
width = input("Enter width")
depth = input("Enter depth")

def cube = (l, w, d):
    volume = l * w * d
    return volume

yourCube = cube(length, width, depth)
print "The volume of your cube is ", yourCube

name = "Mark" #global variable; available everytwhere
age = 43 #global variable; available everytwhere

def greet(x, y):
    print "Hello " x #Hello Mark
    print "You are ", y #You are 43
    print "Hello ", name #Hello Mark
    print "You are ", age #You are 43

greet(name, age)

greet(x, y)
