class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                a=nums[i-1]+1
                return a
        return nums[-1]+1