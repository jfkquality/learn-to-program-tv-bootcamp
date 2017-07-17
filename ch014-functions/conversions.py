def celciusToFahrenheit(temp):
    fahrenheit = temp * (9.0 / 5.0) + 32.0
    return fahrenheit

def fahrenheitToCelsius(temp):
    celsius = (temp - 32.0) * (5.0/9.0)
    return celsius

def showMenu():
    print "A: Convert Celsius to Fahrenheit"
    print "B: Convert Fahrenheit to Celcius"
    print "X: Exit"

showMenu()

option = ""

while option.upper() != "X":
    option = raw_input("Option: ")
    if option.upper() == "A":
        inputTemp = input("Enter the Celsius tempeature to convert: ")
        converted = celciusToFahrenheit(float(inputTemp))
        print "{} degrees Celcius is {} degrees Fahrenheit".format(inputTemp, converted)
    elif option.upper() == "B":
        inputTemp = input("Enter the Fahrenheit temperature to ocnvert: ")
        converted = fahrenheitToCelsius(float(inputTemp))
        print "{} degrees Fahrenheit is {} degrees Celcius".format(inputTemp, converted)
    else:
        print "Please input A, B or X"
    showMenu()
    
