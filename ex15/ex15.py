from sys import argv

script, filename = argv #get the filename from arguments list

txt = open(filename) #open the file, returns the file objext

print "Here is your file %r" % filename #printing out the filename
print txt.read() #reads the returned file object

#repeat with a new filename
print "Type the filename again"
new_filename = raw_input('>')

txt_again = open(new_filename)

print "Here is your file %r" % new_filename
print txt_again.read()