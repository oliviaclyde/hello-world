# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.


word = input("Please enter a sentence: ")

newWord = word.split()

# If I don't assign word.splt() to a new word, then this just reverses all the letters in the word
reverseWord = newWord[::-1]

finalWord = ' '.join(map(str, reverseWord))

print(finalWord)