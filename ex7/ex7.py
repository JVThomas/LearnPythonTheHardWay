print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# * 10 repeats the print operation 10 times
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#note: Shaw states that 80+ characters is bad form in python

word = "'word'"
#basically the comma adds a space on both sides of the inserted var
print "This is a", word, "Notice how it's spaced out!"
#prefer format characters. Easier to implement puntcuation
print "This is a %s Notice how it's spaced out!" %word