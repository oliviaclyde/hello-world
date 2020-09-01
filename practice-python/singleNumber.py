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
        comparisonNumber = nums[0]
        
        for n in range(1, len(nums)):
            # print(n, nums[n])

            if nums[n] == comparisonNumber:
                newList.add(nums[n])
            
            else:
                comparisonNumber = int(nums[n])


        numsNew = set(nums)   
        
        print(numsNew.difference(newList))
        # Result needs to be an int 
        
    

# If equal, make a new array
# Convert both to set
# Compare which element isn't in the new set
# Return that element as int



attempt = Solution()

attempt.singleNumber([4, 1, 2, 1, 2]) 
# attempt.singleNumber([2, 1, 1])
