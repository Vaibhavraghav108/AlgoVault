class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        count=1
        streak=1
        if not nums:
            return 0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]-1:
                streak+=1
            else:
                streak=1
            count=max(count,streak)
        return count