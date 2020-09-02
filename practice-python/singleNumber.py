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
        
        newList = []
        for n in nums:
            if n not in newList:
                newList.append(nums[n])
        
        newList = set(newList)
        result = list(set(nums).difference(newList))
        print(int(result[0]))
        

    


attempt = Solution()

attempt.singleNumber([4, 1, 2, 1, 2]) 
attempt.singleNumber([2, 1, 1])
attempt.singleNumber([5,7,6,7,3,2,2,3,5,6,8,1,9,8,1])