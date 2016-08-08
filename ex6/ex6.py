# assigned string to x passed in values to format characters
x = "There are %d types of people" % 10

#string assignment of binary and don't
binary = "binary"
do_not = "don't"

#assigned string value to y, passed in previous vars
#for format characters
y = "Those who know %s and those who %s" %(binary, do_not)

#prints out x and y
print x
print y

#print out statements, passed in values for format characters
#note: %r returns actual string value, %s return contents
print "I said %r" % x
print "I also said: %s" % y

#boolean assignment
hilarious = False

#note -> I can store placeholders within the var
joke_evaluation = "Isn't that joke so funny?! %r"
# and here I pass in values for the expression
print joke_evaluation % hilarious

#string vars assignment
w = "This is the left side of..."
e = "a string with a right side."

#concatication
print w + e