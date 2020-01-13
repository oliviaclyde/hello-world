# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#Ask user for number of Fibonnaci numbers



def fibNum(): 
    num = int(input("Enter how many Fibonnaci numbers you'd like to see!  "))

    wordList = []

    if num < 0:
        print("Incorrect input")

    elif num == 1:
        wordList = [0]

    elif num == 2:
        wordList = [0, 1]

    elif num > 2:
        n1 = 0
        n2 = 1
        count = 0 
        newList = []
        while count < num:
            newList.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1


    print(newList)



fibNum()



# i = 1

# def num():
#     while (len(list) < a:):
#         list.append[i]        
#     # iterates - list[i] + list[i + 1] = list[i + 2]


        