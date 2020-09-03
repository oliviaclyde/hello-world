# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
wordlist = ['cat','dog','rabbit']
flatList = [aletter for aword in wordlist for aletter in aword]
print(flatList)



# For extra challenge, remove duplicates
letterList = []
flatList = [letterList.append(aletter) for aword in wordlist for aletter in aword if aletter not in letterList]

print(letterList)

