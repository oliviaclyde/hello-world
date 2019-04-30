
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


#Rewrite using b' ' byes instead of UTF-8 strings
"""
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = eval(line.strip())
    cooked_string = next_lang.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors)


    print(cooked_string, "<===>", raw_bytes)

languages = open("languages-bytes-damaged.txt", encoding="utf-8")

main(languages, input_encoding, error)

"""

# New Characters
# UTF-8 : codec; encoding; Unicode Transformation Format 8 Bits (sequence of 8 1s an 0s)
# input_encoding : defining the argv for what encoding standard will be used: i.e. UTF-8, UTF-16 Big5
# "<===>" : just a symbol to show eqivalent values on each side
# encoding : converts a string object to a bytes object using a particular character set encoding
# raw_bytes : line.strip.encode(encoding, errors=errors)
# errors=errors :
# cooked_string : raw_bytes.decode(encoding, errors=errors)
# encoding="utf-8" :
# codec : encoders and decoders; text encodings which encode text to bytes
# decode: decodes the object input and returns a tuple, converts bytes object to a string object
# readline(): read all lines available on the input stream and return them as a list
# line.strip(): returns copy of the string with both leading and trailing characters removed
# error = define the argv for error handling i.e. strict or replace, either allow errors or if you don't allow, then replace what program doesn't know
