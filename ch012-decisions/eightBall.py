# -*- coding: cp1252 -*-
import random

question = raw_input("what is your question? ")
answer = random.randint(1, 20)

print "Question: {}?".format(question)

if answer == 1:
    print "Signs Point To Yes"
elif answer == 2:
    print "Yes"
elif answer == 3:
    print "Reply hazy, try again."
elif answer == 4:
    print "Without a doubt."
elif answer == 5:
    print "All sources say no."
elif answer == 6:
    print "As I see it, yes."
elif answer == 7:
    print "You may rely on it."
elif answer == 8:
    print "Concentrate and ask again."
elif answer == 9:
    print "Outlook not so good."
elif answer == 10:
    print "It is decidedly so."
elif answer == 11:
    print "Better not tell you now."
elif answer == 12:
    print "Very doubtful."
elif answer == 13:
    print "Yes - definitely."
elif answer == 14:
    print "It is certain."
elif answer == 15:
    print "Cannot predict now."
elif answer == 16:
    print "Most likely."
elif answer == 17:
    print "Ask again later."
elif answer == 18:
    print "My reply is no."
elif answer == 19:
    print "Outlook good."
else:
    print "Don�t count on it."
