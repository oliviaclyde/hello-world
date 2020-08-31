# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums) -> int:
        newList = set()
        answer = nums[0]
        
        for n in nums:
            i = 1
            if nums[i] == answer:
                newList.add(n)
            else:
                answer == n
            i += 1


        nums = set(nums)            
        print(nums.difference(newList))
        

# If equal, make a new array
# Convert both to set
# Compare which element isn't in the new set
# Return that element as int



attempt = Solution()

attempt.singleNumber([4, 1, 2, 1, 2])
