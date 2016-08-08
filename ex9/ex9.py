# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"

#new line characters, not unlike ruby
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months

#multi-line printing, lets you set up blocks of strings
#cool thing, picks up on whitespaces and newlines
#set up blocks with triple double quotes, close them the same way
print """
There's something going on here.
    With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#note that %r doesn't interpret special characters
#%r essentially prints out a raw string
print "%r" % months