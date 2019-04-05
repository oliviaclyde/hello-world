formatter = "{} {} {} {}" #defined as a variable with "f-string" inside

print(formatter.format(1, 2, 3, 4)) #this calls the format function and passes the numbers
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
