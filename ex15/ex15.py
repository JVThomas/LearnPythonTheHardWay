from sys import argv

script, filename = argv #get the filename from arguments list

txt = open(filename) #open the file, returns the file objext

print "Here is your file %r" % filename #printing out the filename
print txt.read() #reads the returned file object
txt.close() # close the file when you're done with it

