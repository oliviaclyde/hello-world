# Practice sorting numbers by parcing

# Given a string list: l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# Result should be a string list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

# Write a test to see if it will pass

# versions = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

versions = ["1.0.12", "1.0.2"]

def parseString(l):
    parsed = [item.split(".") for item in l]
    print(parsed)
    listOfNums = [map(int, item) for item in parsed]

    for index, value in enumerate(listOfNums):
        print(list(value))

    
parseString(versions)
