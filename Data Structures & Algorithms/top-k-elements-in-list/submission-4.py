class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        target=sorted(dict,key=dict.get,reverse=True)
        return target[0:k]