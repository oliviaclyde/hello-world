# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.


class Solution:
    def fizzBuzz(self, n):
        numbers = []
        a = 0
        while a < (n+1): 
            numbers.append(a)
            a+=1
        print(numbers)
        
        for num in numbers:
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print (num)
       
        
mySolution = Solution()        

mySolution.fizzBuzz(15)
        
