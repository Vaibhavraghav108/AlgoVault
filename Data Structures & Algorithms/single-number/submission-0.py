class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        return min(dict, key=dict.get)