# Practice sorting numbers by parcing

# Given a string list: l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# Result should be a string list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

# Write a test to see if it will pass

# versions = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]


# Will only work in Python 2.7.16, unsure why it won't run in Python 3.7.2
versions = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

def parseString(l):
    parsed = [item.split(".") for item in l]
    # print(parsed)
    listOfNums = [map(int, item) for item in parsed]
    sortedList = sorted(listOfNums)
    sortedJoined = [('.'.join(str(ii) for ii in item)) for item in sortedList]
    return sortedJoined
   

    
print(parseString(versions))
