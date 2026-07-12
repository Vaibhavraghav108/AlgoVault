class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=nums[0]
        max_sum=nums[0]
        for right in range(1,len(nums)):
            cur_sum=max(nums[right],cur_sum+nums[right])
            max_sum=max(max_sum,cur_sum)
        return max_sum