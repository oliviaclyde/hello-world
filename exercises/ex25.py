#sentence = "All good things come to those who wait."
#words = ex25.break_words(sentence)
def break_words(stuff): #This becomes words = ex25.break_words(sentence)
    """This function will break up words for us."""
    words = stuff.split(' ')
    #This becomes words = sentence.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    #sorted_words = ex25.sort_words(words)
    #ex25.sort_words(ex25.break_words(sentence))
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    #Runs function and passes through sentence which breaks the sentence into individual words and then this function prints 1st word
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    #Runs break_words function and passes sentence variable which breaks the sentence into individual words. This then prints last word.
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    #This returns the words variable, which has been modified to remove 1st and last words
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    #This returns the original sentence which you end up parcing by sentence.split(' ')
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    #This runs the break_words function and passes sentence. Then it sorts alphabetically and prints 1st and last word
    print_first_word(words)
    print_last_word(words)
