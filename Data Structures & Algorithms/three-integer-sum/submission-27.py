class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen=set()
        
        for i in range(0,len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                target=nums[i]+nums[left]+nums[right]
                if target==0:
                    seen.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif target<0:
                    left+=1
                else:
                    right-=1
        return list(i for i in seen) 

