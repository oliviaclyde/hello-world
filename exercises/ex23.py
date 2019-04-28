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




# New Characters
# UTF-8 : codec; encoding
# input_encoding :
# "<===>" :
# encoding : converts a string object to a bytes object using a particular character set encoding
# raw_bytes : line.strip.encode(encoding, errors=errors)
# errors=errors :
# cooked_string : raw_bytes.decode(encoding, errors=errors)
# encoding="utf-8" :
# codec : encoders and decoders; text encodings which encode text to bytes
# decode: decodes the object input and returns a tuple, converts bytes object to a string object
# readline(): read all lines available on the input stream and return them as a list
# line.strip(): returns copy of the string with both leading and trailing characters removed
