#Practice Python
#Exercise 2
#Odd or Even
#nput if types int equality comparison numbers mod


print("Hello. Welcome to the number predictor!")
# response = int(print(input("Please enter a number\n>  ")))
r = input("Please enter a number: \n> ")

if int(r) % 2 == 0:
    if int(r) % 4 == 0:
        print("Your number is even AND divisible by 4!")
    else:
        print("Your number is even!")
else:
    print("Your number is odd!")

print("Please enter two numbers: ")
num = input(">  ")
check = input(">  ")

if int(num) % int(check) == 0:
    print("Your second number divides evenly into your first!")
else:
    print("Your numbers don't divide into eachother evenly.")
