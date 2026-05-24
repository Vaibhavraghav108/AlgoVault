class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        streak=1
        lst=sorted(set(nums))
        if not nums:
            return 0
        for i in range(1,len(lst)):
            if lst[i]==lst[i-1]+1:
                count+=1
            else:
                count=1
            streak=max(streak,count)
        return streak