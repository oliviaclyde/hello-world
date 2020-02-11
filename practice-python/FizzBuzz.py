# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.


class Solution:
    def fizzBuzz(self, n):
        numbers = []
        
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                numbers.append("FizzBuzz")
            elif num % 3 == 0:
                numbers.append("Fizz")
            elif num % 5 == 0:
                numbers.append("Buzz")
            else:
                numbers.append(str(num))

        print(numbers)

mySolution = Solution()        

mySolution.fizzBuzz(15)
        
