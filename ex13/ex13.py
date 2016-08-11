from sys import argv # import statement, holds arguments
					 # first argument is always the name of the module
					 # in this case its the name of the file, ex13.py
					 #rest of the arguments follow, assigned based on order it was written on CLI


script, first, second, third = argv #assignment essentially unpacks variables

print "The script is called", script
print "Your first variable is called:" , first
print "Your second variable is called:", second
print "Your third variable is called:", third