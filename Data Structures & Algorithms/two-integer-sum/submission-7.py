class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            result=target-nums[i]
            if result in dict:
                return [dict[result],i]
            dict[nums[i]]=i
        return [-1,-1]