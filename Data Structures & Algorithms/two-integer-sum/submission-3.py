class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            t=target-nums[i]
            if t in dict:
                return [dict[t],i]
            dict[nums[i]]=i
        return [-1,-1]

    