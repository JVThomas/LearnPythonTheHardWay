print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()

#no comma? input shows up on new line
print "How much do you weigh?"
weight = raw_input()

#same deal here, using %r to print out the raw values
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#New concept learned: raw_input()
#Essentially takes in user input
#think ruby's gets.chomp / gets.strip
#also means it'll come in as a string

#Another new concept :
	#putting a comma after a prompt allows the input to appear on the same line
	#take out the comma, input shows up on next line