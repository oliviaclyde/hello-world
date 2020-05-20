# Ask the user for a number and determine whether the number is prime or not.

def isPrime(num):
    if num <= 0:
        print("Not prime.")
    elif num == 1:
        print("Your number is 1 and not considered prime!")
    elif num == 2:
        print("Your number is prime!")
    else:
        # prime == true
        # This range will go to the number just before our number
        # Don't need to check 1 or the number itself, since we know prime numbers are divisible by 1 and themselves
        for i in range(2, num):
            if num % i == 0:
                # return prime == false
                print(num, "is NOT a prime number.")
                break
        else:
            print(num, "is a prime number.")
    

num = int(input("Please enter a number: "))
isPrime(num)

