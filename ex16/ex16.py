from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN"
raw_input("Enter your choice now")

print "Opening the file"
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("Enter line 1 ")
line2 = raw_input("Enter line 2 ")
line3 = raw_input("Enter line 3 ")

print "I'm going to write the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close the file"

target.close()
