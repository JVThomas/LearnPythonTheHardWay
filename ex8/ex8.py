formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
#this will print out the string representation of the formatter
#basically it'll print out the format values
print formatter % (formatter, formatter, formatter, formatter)

#added this line, I can still pass in values to internal formatters
print formatter % ((formatter % (1,2,3,4), formatter, formatter % ('one', 'two', 'three', 'four'), formatter))
#same deal as previous examples, commas add spaces within the string
print formatter % (
	"I has this thind.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)