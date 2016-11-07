from sys import argv
from os.path import exists

script, input_file, output_file = argv

print "Copying from %s to %s" % (input_file,output_file)

#use semi-colons to seperate multiple lines of code. Good to fit shortliners on one line
input_data = open(input_file); input_text = input_data.read()

print "The input file is %d bytes long" % len(input_text)

#exists checks to see if a file exists
print "Does the output file exist? %r" % exists(output_file)

print "Hit RETURN to continue, otherwise hit CTRL-C to abort"

raw_input("Enter your choice now ")

output_file = open(output_file, 'w'); output_file.write(input_text)

print "Alright, done!"

#general rule of thumb for any language: close file when done with it
output_file.close()
input_data.close()

print "Goodbye!"
