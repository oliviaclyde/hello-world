# # Ask the user for a string and print out whether this string is a palindrome or not. 
# # (A palindrome is a string that reads the same forwards and backwards.)

#1st way: convert to string and reverse order
a = "qwertytrewq"
b = str(a)[::-1]


def isPalindrome():
    if a == b:
        print("Your string is a palindrome!")
    else:
        print("Your string is NOT a palindrome!")


isPalindrome()




#2nd way: convert to list, reverse, join back to string and compare equality 
def checkPalindrome():
    a = str(input("Please enter a string of letters: "))
    newA = list(a)
    b = (newA[::-1])
    
    (''.join(newA))
    (''.join(b))

    if newA == b:    
        print("Is Palindrome!") 
    else: 
        print("NOT Palindrome.")

checkPalindrome()