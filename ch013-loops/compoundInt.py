invest = input("How much are you planning to invest? ")
term = input("How many years are you going to invest the money? ")
intRate = input("Input the annual interest rate as a decimaal. ")


print "Month\tInterest Earned\tTotal"

month = 1
while month <= term * 12:
    interestEarned = invest * intRate / 12
    invest = interestEarned + invest
    print "{}\t$ {:.2f}\t$ {:.2f}".format(month, interestEarned, invest)
    print "{}".format(month), "\t", "$", "{:.2f}".format(interestEarned), "\t", "$", "{:.2f}".format(invest)
    month = month + 1
