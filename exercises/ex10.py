#Escape sequences \
#

#Other esacpe sequences
#\t = tab in the line
tabby_cat = "\tI'm tabbed in."
#\n = new line
persian_cat = "I'm split\non a line."
# \\ = Added a slash and space between words
backslash_cat = "I'm \\ a \\ cat."

#Triple quotes = commented out
#\t* = creates a tabbed list with a * as the marker
#Pay attention to the last example, the line was tabbed and a list and then put on a new line "Grass" tabbed in
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Additional Notes
#Escape     What it does
#  \\       Backslash
#  \'       Single-quote
#  \"       Double-quote
#  \a       ASCII bell (BEL)(warning or alert)
#  \b       ASCII backspace (BS)
#  \f       ASCII formfeed (FF)
#  |n       ASCII linefeed (LF) (returns to new line)
#  \N{name} Character named in the Unicode database (Unicode only)
#  \r       Carriage return (CR)
#  \t       Horizontal tab (TAB)
#  \uxxxx    Character with 16-bit hex value xxxx
#  \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
#  \v       ASCII verticle tab (VT)
#  \000     Character with octal value 000
#  \xhh     Character with hex value hh

#Additional practice exercies
#Combining escape sequences and formats

counting = "{}"
print(counting.format(1))
advice = "You can do all the hard things.\n\tJust don't give up!"
print(advice)
#\r defines the start of the line of text. Text before this won't print
carriage_return = "I am \rwondering how this carriage return works."
print(carriage_return)
#Will pass through items in the list and tab over the first and print the following two on new lines
items_for_sale = "{} {} {}"
print(items_for_sale.format("\tshoes", "\nshirt", "\npants"))
