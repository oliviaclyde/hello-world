#Importing from sys module
from sys import argv
#Importing from the os.path module a new package called "exists"
from os.path import exists

#Defining 3 variables assigned to argv
script, from_file, to_file = argv
"""
#Print statement calling a format and passing two variables
print(f"Copying from {from_file} to {to_file}")
"""
#We could do these two on one line, how?
indata = open(from_file).read()
"""
in_file = open(from_file)
indata = in_file.read()
"""
"""
print(f"The input file is {len(indata)} bytes long")
"""
print(f"Does the output file exist? {exists(to_file)}")
"""print("Ready, hit RETURN to continue. CTRL-C to abort.")
input()"""

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

#Closing files frees up resources and any attempt to use the file object will fail
out_file.close()
#Don't need the following line now that we opened and put the read command on the file. It closes after this command is executed
#in_file.close()

#Trying to re-write the script in a more condensed version from line 10 onwards
#Remove line 10, not needed
#Remove line 19, not needed
#Remove Line 22 and 23, not needed
