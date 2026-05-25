class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        left=0
        right=1
        while(right<len(prices)):
            if prices[left]>prices[right]:
                left=right
            else:
                profit=prices[right]-prices[left]
                count=max(count,profit)
            right+=1
        return count