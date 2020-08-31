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
